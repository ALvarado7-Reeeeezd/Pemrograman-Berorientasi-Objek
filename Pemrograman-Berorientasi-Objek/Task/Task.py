class Mahasiswa:
    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = nilai

    def cek_status(self):
        if self.nilai >= 75:
            return "Lulus"
        else:
            return "Tidak Lulus"

    def tampilkan_data(self):
        print("Nama    :", self.nama)
        print("NIM     :", self.nim)
        print("Jurusan :", self.jurusan)
        print("Nilai   :", self.nilai)
        print("Status  :", self.cek_status())
        print("------------------------")


# Membuat object mahasiswa
mhs1 = Mahasiswa("Fandi", "2595114028", "Teknik Informatika (B)", 80)
mhs2 = Mahasiswa("Gilang", "2595114026", "Teknik Informatika (B)", 70)
mhs3 = Mahasiswa("Syahrul", "2595114021", "Sistem Informasi (B)", 90)

# Menampilkan data
mhs1.tampilkan_data()
mhs2.tampilkan_data()
mhs3.tampilkan_data()