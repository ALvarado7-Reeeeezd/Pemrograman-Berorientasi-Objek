# Tugas Mandiri: Python Advanced Topics

## Identitas Mahasiswa
- **Nama:** ALVARADO VAREZA
- **NIM:** 2595114025
- **Kelas:** B
- **Mata Kuliah:** TEKNIK INFORMATIKA

## Deskripsi
Repository ini berisi penyelesaian tiga studi kasus pada tugas mandiri Python Advanced Topics. Setiap studi kasus ditempatkan di folder terpisah dan memiliki file `main.py`, README, serta screenshot output terminal.

## Daftar Studi Kasus

### 1. Analisis Nilai Mahasiswa
Folder: [`case-01-analisis-nilai/`](case-01-analisis-nilai/)

Menghitung nilai akhir mahasiswa menggunakan bobot tugas 30%, UTS 30%, dan UAS 40%. Program juga memfilter mahasiswa dengan nilai akhir di atas 80, mengurutkan ranking dari nilai tertinggi ke terendah, dan menampilkan detail mahasiswa terbaik.

Konsep utama: list of dictionaries, List Comprehension, lambda function, filtering, dan `sorted()`.

### 2. Streaming Data Sensor IoT Hemat Memori
Folder: [`case-02-iot-generator/`](case-02-iot-generator/)

Mensimulasikan 10 pembacaan suhu dalam rentang 15,0°C hingga 38,0°C. Data dihasilkan dan diproses satu per satu, lalu dikategorikan menjadi Dingin, Normal, atau Panas.

Konsep utama: generator function, `yield`, `next()`, iterator/iterable, dan pemrosesan data bertahap.

### 3. Sistem Keamanan Akun dan Audit Log Login
Folder: [`case-03-login-security/`](case-03-login-security/)

Memvalidasi format username dan password, mengelola kredensial melalui class `User` dengan `@property`, serta mencatat waktu, username, status login, dan alasan penolakan menggunakan decorator audit log.

Konsep utama: modul `re` untuk RegEx, class dan property, decorator, exception handling, serta audit log tanpa mencatat password asli.

## Cara Menjalankan
Pastikan Python sudah terpasang. Buka terminal VS Code di folder repository, kemudian jalankan salah satu perintah berikut:

```powershell
py .\case-01-analisis-nilai\main.py
py .\case-02-iot-generator\main.py
py .\case-03-login-security\main.py
```

