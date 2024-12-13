## Gambaran Umum
PlantScan adalah sebuah aplikasi inovatif yang dirancang untuk membantu pengguna mengidentifikasi tanaman dan memberikan informasi terkait perawatan tanaman tersebut. Dengan memanfaatkan teknologi machine learning berbasis TensorFlow Keras, PlantScan memungkinkan pengguna untuk memfoto tanaman menggunakan aplikasi mobile, lalu menerima hasil analisis secara langsung.

## Fitur Utama

### 1. Upload Gambar Tanaman
- Pengguna dapat mengunggah gambar tanaman melalui API.
- Gambar yang diunggah akan diproses untuk analisis lebih lanjut.

### 2. Analisis Berbasis Machine Learning
- Menggunakan model TensorFlow Keras yang telah dilatih untuk klasifikasi atau deteksi penyakit pada tanaman.
- Proses analisis dilakukan di backend Flask.

### 3. Hasil Diagnosa
- API mengembalikan hasil analisis yang mencakup:
  - Informasi kesehatan tanaman (sehat atau terkena penyakit).
  - Saran perawatan jika diperlukan.

### 4. Integrasi dengan Aplikasi Mobile
- API dirancang untuk integrasi dengan aplikasi mobile, memungkinkan pengguna mengakses layanan analisis secara langsung dari perangkat seluler.

## Teknologi yang Digunakan

### 1. Flask Framework
- Digunakan untuk membangun API backend.
- Menangani permintaan dari aplikasi mobile dan mengirimkan hasil analisis.

### 2. TensorFlow Keras
- Model deep learning yang dilatih menggunakan TensorFlow Keras.
- Digunakan untuk menganalisis gambar tanaman yang diunggah oleh pengguna.

### 3. REST API
- API berbasis HTTP untuk menerima gambar dan mengirimkan hasil analisis.
- Dapat diintegrasikan dengan berbagai platform, termasuk aplikasi mobile.

## Alur Kerja Program

1. **Pengguna Mengunggah Gambar**
   - Gambar tanaman diunggah melalui aplikasi mobile yang terhubung ke API.

2. **Backend Flask Memproses Gambar**
   - Flask menerima gambar dari aplikasi mobile dan memvalidasi input.

3. **Model TensorFlow Keras Membuat Prediksi**
   - Gambar dikirim ke model machine learning untuk diproses.
   - Model memberikan hasil analisis, seperti kondisi kesehatan tanaman atau jenis penyakit yang terdeteksi.

4. **Hasil Analisis Dikembalikan ke Pengguna**
   - API mengembalikan hasil diagnosa ke aplikasi mobile dalam format JSON.
   - Pengguna dapat melihat hasil analisis secara langsung di aplikasi.

## Instalasi

Untuk menginstal dan menjalankan aplikasi, ikuti langkah-langkah berikut:

1. **Clone repositori:**
   ```bash
   git clone https://github.com/ridwanijazz/PlantScan-Flask.git
2. **Masuk ke direktori proyek:**
    ```bash
    cd PlantScan-Flask
3. **Instal dependensi:**
    ```bash
    pip install -r requirements.txt
4. **Jalankan aplikasi:**
   ```bash
   python <nama-api>.py
   
## Penggunaan API
Untuk menggunakan API, kirim permintaan POST ke endpoint /upload dengan file gambar.

1. **Contoh Permintaan**
   ```bash
    curl -X POST -F 'file=@path_to_image.jpg' http://localhost:8080/upload
2. **Contoh Respons**
  ```bash
  {
      "health_status": "sehat",
      "care_suggestions": "Tidak ada tindakan yang diperlukan."
  }
