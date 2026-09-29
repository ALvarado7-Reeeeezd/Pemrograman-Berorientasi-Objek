
class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_data(self):
        print("Nama Kendaraan :", self.nama)
        print("Merk           :", self.merk)
        print("Tahun          :", self.tahun)
        print("Kecepatan      :", self.kecepatan, "km/jam")


class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jumlah Kursi   :", self.jumlah_kursi)


class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Tipe Motor     :", self.tipe_motor)


# Membuat object kendaraan
mobil1 = Mobil("GT-R (R35)", "Nissan", 2026, 315, 4)
motor1 = Motor("Ninja ZX-25R", "Kawasaki", 2024, 180, "Sport")

# Menampilkan data
print("=== DATA MOBIL ===")
mobil1.tampilkan_data()

print("\n=== DATA MOTOR ===")
motor1.tampilkan_data()