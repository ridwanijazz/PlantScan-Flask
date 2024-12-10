from flask import Flask, render_template, request
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np

app = Flask(__name__)

# Memuat model buatan sendiri
model = load_model('./tomato.h5')

@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
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

    # Mengasumsikan output model berupa probabilitas untuk dua kelas (sehat/sakit)
    class_names = ['sehat', 'sakit']  # Pastikan sesuai dengan label model
    predicted_class = class_names[np.argmax(yhat)]  # Memilih kelas dengan probabilitas tertinggi
    confidence = np.max(yhat) * 100  # Menghitung tingkat kepercayaan dalam persentase

    # Menampilkan hasil klasifikasi
    classification = '%s (%.2f%%)' % (predicted_class, confidence)

    return render_template('index.html', prediction=classification)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
