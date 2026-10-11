# Studi Kasus 1 — Analisis Nilai Mahasiswa

## Tujuan
Program mengolah data nilai mahasiswa, menghitung nilai akhir berdasarkan bobot resmi, menampilkan mahasiswa dengan nilai akhir di atas 80, membuat ranking, dan menampilkan detail mahasiswa terbaik.

## Aturan Perhitungan
- Tugas: 30%
- UTS: 30%
- UAS: 40%

Rumus nilai akhir:

```text
Nilai Akhir = (Tugas × 0,30) + (UTS × 0,30) + (UAS × 0,40)
```

Data disimpan dalam bentuk list of dictionaries. Program menggunakan contoh mahasiswa dari soal dan menambahkan dua data mahasiswa.

## Konsep Python yang Digunakan
- **List of dictionaries:** menyimpan data setiap mahasiswa dalam bentuk pasangan kunci dan nilai.
- **List Comprehension:** membentuk data baru sekaligus menghitung nilai akhir setiap mahasiswa.
- **Filtering:** memilih mahasiswa yang nilai akhirnya benar-benar lebih besar dari 80.
- **Lambda Function:** menentukan `nilai_akhir` sebagai kunci pengurutan.
- **`sorted()`:** mengurutkan seluruh mahasiswa dari nilai akhir tertinggi ke terendah dengan `reverse=True`.
- **`enumerate()`:** memberi nomor pada setiap peringkat.

## Cara Menjalankan
Buka terminal VS Code di folder utama repository, lalu jalankan:

```powershell
py .\case-01-analisis-nilai\main.py
```

Atau, jika terminal sudah berada di folder `case-01-analisis-nilai`, jalankan:

```powershell
py main.py
```

Jika perintah `py` tidak tersedia, gunakan `python` sebagai penggantinya.

## Output
Program menampilkan daftar nilai akhir, mahasiswa berprestasi, ranking seluruh mahasiswa, dan detail mahasiswa terbaik.

Screenshot output terminal disimpan sebagai [`output.png`](output.png). Pastikan file tersebut merupakan tangkapan layar nyata dari hasil program yang sudah dijalankan.