from flask import Flask, render_template, request, jsonify
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from collections import OrderedDict
import numpy as np
import uuid
import os
from datetime import datetime
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Memuat model buatan sendiri
model = load_model('./grape_model.h5')



@app.route('/', methods=['POST', 'GET'])
def predict():
    try:
        if request.method == 'POST':
            # Memastikan file gambar ada di request
            if 'imagefile' not in request.files:
                raise ValueError("No image file found in the request.")

            imagefile = request.files['imagefile']
            print(imagefile)

            # Validasi file tidak kosong
            if imagefile.filename == '':
                raise ValueError("The uploaded image file is empty.")

            # image_path = "./images/" + imagefile.filename
            # imagefile.save(image_path)

            # Memuat dan mengubah ukuran gambar sesuai dengan input model
            image = Image.open(BytesIO(imagefile.read()))
            image = image.resize((150,150))  # Sesuaikan dengan ukuran input model Anda
            image = img_to_array(image)
            image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))  # Menyesuaikan dimensi input

            # Melakukan prediksi
            yhat = model.predict(image)

            # Mengasumsikan output model berupa probabilitas untuk beberapa kelas
            class_names = ["Black Rot", "ESCA", "Healthy", "Leaf Blight"]  # Pastikan sesuai dengan label model
            predicted_class = class_names[np.argmax(yhat)]  # Memilih kelas dengan probabilitas tertinggi

            
            # Description and actions based on class
            if predicted_class == "Black Rot":
                description = "Brown spots on leaves, stem lesions, and mummified grapes. Spreads via wind or rain-borne spores in humid, warm conditions."
                action = "Use copper-based or strobilurin fungicides at the early infection stage. Rotate fungicides to prevent resistance."
            elif predicted_class == "ESCA":
                description = "Yellow-brown leaf spots, burned edges, wood rot, and sudden wilting, mainly in older grapevines."
                action = "Removing and burning infected parts can slow the spread."
            elif predicted_class == "Leaf Blight":
                description = "Brown or black leaf spots that turn into dead areas, often leading to early leaf drop. Reduces photosynthesis and crop yield."
                action = "Apply fungicides to young leaves during the growing season or use chlorothalonil to help control the infection."
            elif predicted_class == "Healthy":
                description = "Fresh green leaves, free of spots or necrosis. Growth is uniform, and fruit develops without deformities or damage."
                action = "Prune regularly to remove old leaves or branches. Fertilize balanced with adequate nitrogen, phosphorus, and potassium."
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
