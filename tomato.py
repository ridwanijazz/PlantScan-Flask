from flask import Flask, render_template, request, jsonify
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import uuid
from datetime import datetime

app = Flask(__name__)

# Memuat model buatan sendiri
model = load_model('./model/chili_model.h5')

@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    try:
        # Memastikan file gambar ada di request
        if 'imagefile' not in request.files:
            raise ValueError("No image file found in the request.")

        imagefile = request.files['imagefile']

        # Validasi file tidak kosong
        if imagefile.filename == '':
            raise ValueError("The uploaded image file is empty.")

        image_path = "./images/" + imagefile.filename
        imagefile.save(image_path)

        # Memuat dan mengubah ukuran gambar sesuai dengan input model
        image = load_img(image_path, target_size=(150, 150))  # Sesuaikan dengan ukuran input model Anda
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))  # Menyesuaikan dimensi input
        
        # Jika model memerlukan preprocess_input, aktifkan ini
        # image = preprocess_input(image)  # Hapus jika tidak diperlukan

        # Melakukan prediksi
        yhat = model.predict(image)

        # Mengasumsikan output model berupa probabilitas untuk beberapa kelas
        class_names = ["bacterial", "early", "mold", "target spot", "yellow", "healthy"]  # Pastikan sesuai dengan label model
        predicted_class = class_names[np.argmax(yhat)]  # Memilih kelas dengan probabilitas tertinggi

        # Menyusun response dalam format JSON
        response = {
            "status": "success",  # Status umum (bisa ganti jadi 'failed' jika perlu)
            "status_code": 200,  # Kode status HTTP
            "id": str(uuid.uuid4()),  # ID unik untuk permintaan ini
            "createdAt": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Waktu pembuatan
            "label": predicted_class,  # Hasil deteksi
            "message": "The image was successfully processed and classified."  # Pesan tindak lanjut
        }

        return jsonify(response)

    except Exception as e:
        # Menyusun response untuk error
        response = {
            "status": "failed",
            "status_code": 400,  # Bad Request
            "message": str(e)
        }
        return jsonify(response), 400  # Mengembalikan status HTTP 400

# Penanganan error global untuk route yang tidak ditemukan
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({
        "status": "failed",
        "status_code": 404,
        "message": "The requested resource was not found."
    }), 404

# Penanganan error global untuk error server
@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "status": "failed",
        "status_code": 500,
        "message": "An internal server error occurred. Please try again later."
    }), 500

if __name__ == '__main__':
    app.run(port=3000, debug=True)
