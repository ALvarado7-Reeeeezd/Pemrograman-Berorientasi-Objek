# Studi Kasus 2: Streaming Data Sensor IoT Hemat Memori

import random


def generator_pembacaan_suhu(jumlah_pembacaan):
    """Menghasilkan suhu satu per satu, bukan mengumpulkan semuanya dalam list."""
    for _ in range(jumlah_pembacaan):
        # Simulasi satu pembacaan suhu antara 15.0°C hingga 38.0°C.
        yield round(random.uniform(15.0, 38.0), 1)


def kategori_suhu(suhu):
    """Mengembalikan kategori sesuai batas yang ditetapkan di soal."""
    if suhu < 20:
        return "Dingin"
    elif suhu <= 30:
        return "Normal"
    else:
        return "Panas"


JUMLAH_PEMBACAAN = 10
sensor = generator_pembacaan_suhu(JUMLAH_PEMBACAAN)

print("=" * 48)
print("       STREAMING DATA SENSOR SUHU IoT")
print("=" * 48)
print(f"{'No.':<5}{'Suhu':<15}{'Kategori':<15}")
print("-" * 48)

# next(sensor) meminta satu nilai suhu dari generator setiap iterasi.
# Tidak ada list besar yang menampung seluruh pembacaan.
for nomor in range(1, JUMLAH_PEMBACAAN + 1):
    suhu = next(sensor)
    status = kategori_suhu(suhu)
    print(f"{nomor:<5}{suhu:>5.1f} °C{'':<7}{status:<15}")

print("-" * 48)
print(f"Selesai: {JUMLAH_PEMBACAAN} pembacaan diproses satu per satu.")