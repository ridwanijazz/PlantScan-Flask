from flask import Flask, render_template, request, jsonify
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from collections import OrderedDict
import numpy as np
import uuid
import os
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
        if request.method == 'POST':
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

            # Melakukan prediksi
            yhat = model.predict(image)

            # Mengasumsikan output model berupa probabilitas untuk beberapa kelas
            class_names = ["healthy", "yellow", "leaf curl"]  # Pastikan sesuai dengan label model
            predicted_class = class_names[np.argmax(yhat)]  # Memilih kelas dengan probabilitas tertinggi

            # Deskripsi dan tindakan berdasarkan kelas
            if predicted_class == "healthy":
                description = "Chili plant leaves are healthy, vibrant green, with normal texture, no signs of damage or disease, and optimal growth."
                action = "Continue regular care: water 1-2 times daily (morning or evening), add compost or manure every 2 weeks, and ensure 4-6 hours of sunlight daily."
            elif predicted_class == "yellow":
                description = "Yellowing leaves in chili plants, usually starting from the bottom, can be caused by nutrient deficiencies (like nitrogen or iron), overwatering, or diseases such as Fusarium wilt."
                action = "To fix nutrient deficiency, use rice water or organic liquid fertilizer. For overwatering, water once a day or when the soil dries. Remove yellow leaves to prevent disease spread."
            elif predicted_class == "leaf curl":
                description = "Chili leaves curl or bend, often turning yellow or brown at the edges. Common causes include pests (like thrips or mites), viral infections (such as Chili Leaf Curl Virus), or nutrient deficiencies."
                action = "For pest control, spray leaves with liquid soap solution or garlic water, and if nutrient deficiency occurs, water with rice wash or add organic fertilizer."
            else:
                description = "Unknown class"
                action = "No action available"

            # Menyusun response dalam format JSON
            response = OrderedDict({
                "status": "success",
                "status_code": 200,
                "id": str(uuid.uuid4()),
                "createdAt": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "label": predicted_class,
                "description": description,
                "action": action,
                "message": "The image was successfully processed and classified."
            })

            return jsonify(response)

        return jsonify({
            "status": "success",
            "message": "Please upload an image for prediction."
        }), 200

    except Exception as e:
        # Menyusun response untuk error
        response = {
            "status": "failed",
            "status_code": 400,  # Bad Request
            "message": str(e)
        }
        return jsonify(response), 400

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
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)