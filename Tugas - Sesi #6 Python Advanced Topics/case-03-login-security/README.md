# Studi Kasus 3 — Sistem Keamanan Akun dan Audit Log Login

## Tujuan
Program memvalidasi kredensial pengguna, memodelkan akun dengan class `User`, dan membuat audit log untuk setiap percobaan login. Log mencatat waktu, username, status login, serta alasan penolakan jika login gagal. Password asli tidak dicetak atau ditulis ke audit log.

## Aturan Validasi
- **Username:** minimal 5 karakter dan hanya terdiri dari huruf serta angka; spasi dan simbol tidak diperbolehkan.
- **Password:** minimal 8 karakter dan wajib mengandung setidaknya satu angka.
- Validasi format menggunakan ekspresi reguler (RegEx) dari modul bawaan `re`.

## Konsep Python yang Digunakan
- **RegEx (`re`):** memeriksa apakah username dan password memenuhi pola yang ditentukan.
- **Class `User`:** merepresentasikan akun pengguna.
- **`@property` dan setter:** mengatur pembacaan serta validasi nilai username dan password melalui atribut, dengan penyimpanan internal pada `_username` dan `_password`.
- **Decorator:** `audit_login` membungkus fungsi `login` agar hasil percobaan tercatat tanpa mencampur kode pencatatan dengan logika autentikasi utama.
- **Timestamp:** `datetime.now()` mencatat waktu percobaan login.
- **Exception handling:** `ValueError` digunakan untuk menyampaikan alasan kredensial ditolak dan ditangani oleh decorator untuk audit log.

## Skenario Pengujian
1. Login ditolak karena username mengandung simbol atau spasi yang tidak diperbolehkan.
2. Login ditolak karena password terlalu pendek.
3. Login ditolak karena password tidak mengandung angka.
4. Login berhasil saat username dan password memenuhi aturan serta cocok dengan akun demo yang terdaftar.

Akun yang digunakan adalah akun demo di dalam program. Jangan menggantinya dengan password pribadi.

## Cara Menjalankan
Buka terminal VS Code di folder utama repository, lalu jalankan:

```powershell
py .\case-03-login-security\main.py
```

Atau, jika terminal sudah berada di folder `case-03-login-security`, jalankan:

```powershell
py main.py
```

Jika perintah `py` tidak tersedia, gunakan `python` sebagai penggantinya.

## Output dan Keamanan Log
Program menampilkan hasil empat skenario pengujian beserta timestamp dan status audit. Password tidak dimasukkan ke pesan audit log.

Screenshot output terminal disimpan sebagai [`output.png`](output.png). Pastikan file tersebut merupakan tangkapan layar nyata dari hasil program yang sudah dijalankan.