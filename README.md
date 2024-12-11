# Gambaran Umum Program
PlantScan-Flask adalah sebuah API berbasis Flask, framework Python untuk pengembangan aplikasi web. Program ini dirancang untuk melakukan analisis tanaman menggunakan model machine learning berbasis TensorFlow Keras. Tujuan utama program ini adalah untuk memproses gambar tanaman, menganalisisnya, dan memberikan hasil diagnosa yang nantinya dapat diakses melalui aplikasi mobile.

## Fitur Utama Program

### Upload Gambar Tanaman
- Pengguna dapat mengunggah gambar tanaman melalui API.
- Gambar ini akan diproses untuk analisis lebih lanjut.

### Analisis Berbasis Machine Learning
- Program menggunakan model TensorFlow Keras yang telah dilatih untuk melakukan klasifikasi atau deteksi penyakit pada tanaman.
- Model ini diproses dalam backend Flask.

### Hasil Diagnosa
- API mengembalikan hasil analisis, seperti:
  - Jenis tanaman yang terdeteksi.
  - Informasi kesehatan tanaman (sehat atau terkena penyakit).
  - Saran perawatan jika diperlukan.

### Integrasi dengan Aplikasi Mobile
- API ini dirancang untuk diintegrasikan dengan aplikasi mobile sehingga pengguna dapat mengakses layanan analisis secara langsung dari perangkat seluler.

## Teknologi yang Digunakan

### Flask Framework
- Digunakan untuk membangun API backend.
- Menangani request dari aplikasi mobile dan mengirimkan hasil analisis.

### TensorFlow Keras
- Model deep learning dilatih menggunakan TensorFlow Keras.
- Model ini digunakan untuk menganalisis gambar tanaman yang diunggah pengguna.

### REST API
- API berbasis HTTP untuk menerima gambar dan mengirimkan hasil analisis.
- Dapat diintegrasikan dengan berbagai platform, termasuk aplikasi mobile.

### Aplikasi Mobile
- API ini akan diimplementasikan ke dalam aplikasi mobile (mungkin menggunakan Flutter, React Native, atau framework lainnya).

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
   - Pengguna dapat melihat hasil analisis langsung di aplikasi.

