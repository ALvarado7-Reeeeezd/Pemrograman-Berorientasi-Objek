# Studi Kasus 2 — Streaming Data Sensor IoT Hemat Memori

## Tujuan
Program menyimulasikan pembacaan suhu sensor IoT sebanyak 10 kali. Setiap suhu dihasilkan dan diproses satu per satu tanpa mengumpulkan seluruh pembacaan ke dalam list besar.

## Aturan Kategori Suhu
- **Dingin:** suhu di bawah 20°C.
- **Normal:** suhu dari 20°C sampai dengan 30°C.
- **Panas:** suhu di atas 30°C.

Nilai suhu simulasi dibuat dalam rentang 15,0°C hingga 38,0°C. Karena program memakai nilai acak, hasil suhu dapat berbeda pada setiap eksekusi.

## Konsep Python yang Digunakan
- **Generator function:** fungsi `generator_pembacaan_suhu()` menghasilkan nilai suhu bertahap.
- **`yield`:** mengembalikan satu nilai suhu dan menunda kelanjutan fungsi sampai nilai berikutnya diminta.
- **Generator dan `next()`:** `next(sensor)` meminta satu pembacaan dari generator.
- **Iterator/iterable:** program mengonsumsi nilai melalui objek generator yang dapat diiterasi.
- **Efisiensi memori:** program tidak menyimpan semua pembacaan suhu ke dalam satu list besar; satu nilai diproses pada satu waktu.

Penghematan memori bergantung pada ukuran dan cara pengolahan data. Untuk simulasi kecil ini dampaknya mungkin tidak terasa, tetapi pola generator berguna untuk aliran data yang besar atau panjang.

## Cara Menjalankan
Buka terminal VS Code di folder utama repository, lalu jalankan:

```powershell
py .\case-02-iot-generator\main.py
```

Atau, jika terminal sudah berada di folder `case-02-iot-generator`, jalankan:

```powershell
py main.py
```

Jika perintah `py` tidak tersedia, gunakan `python` sebagai penggantinya.

## Output
Program menampilkan nomor pembacaan, nilai suhu, dan kategori suhu untuk 10 pembacaan berturut-turut.

Screenshot output terminal disimpan sebagai [`output.png`](output.png). Pastikan file tersebut merupakan tangkapan layar nyata dari hasil program yang sudah dijalankan.