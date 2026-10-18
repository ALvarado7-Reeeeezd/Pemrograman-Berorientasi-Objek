BOBOT_TUGAS = 30
BOBOT_UTS = 30
BOBOT_UAS = 40
NILAI_LULUS = 60

class PenilaianMahasiswa:
    def __init__(self, nama, nim, nilai_tugas, nilai_uts, nilai_uas):
        if nim.strip() == "" or nama.strip() == "":
            raise ValueError("NIM dan Nama tidak boleh kosong.")
        self.nim = nim
        self.nama = nama
        self.nilai_tugas =self.validasi_nilai(nilai_tugas, "Nilai Tugas")
        self.nilai_uts = self.validasi_nilai(nilai_uts, "Nilai UTS")
        self.nilai_uas = self.validasi_nilai(nilai_uas, "Nilai UAS")

    def validasi_nilai(self, nilai, nama_komponen):
        if nilai < 0 or nilai > 100:
            raise ValueError(f"{nama_komponen} harus antara 0 sampai 100.")
        return nilai

    def hitung_nilai_akhir(self):
        total = (self.nilai_tugas * BOBOT_TUGAS
                + self.nilai_uts * BOBOT_UTS
                + self.nilai_uas * BOBOT_UAS)
        return total / 100

    def tentukan_grade(self):
        nilai_akhir = self.hitung_nilai_akhir()
        if nilai_akhir >= 85:
            return "A"
        elif nilai_akhir >= 75:
            return "B"
        elif nilai_akhir >= 65:
            return "C"
        elif nilai_akhir >= 50:
            return "D"
        else:
            return "E"

    def tentukan_status(self):
        nilai_akhir = self.hitung_nilai_akhir()
        if nilai_akhir >= NILAI_LULUS:
            return "Lulus"
        else:
            return "Tidak Lulus"

    def cetak_hasil(self):
        nilai_akhir = self.hitung_nilai_akhir()
        grade = self.tentukan_grade()
        status = self.tentukan_status()
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Nilai Akhir: {nilai_akhir:.2f}")
        print(f"Grade: {self.tentukan_grade()}")
        print(f"Status: {self.tentukan_status()}")
        print("================================")    

def baca_angka(label):
    """Membaca input angka; kalau bukan angka, lempar Value Error dengan pesan yang sesuai."""
    teks = input(f"{label}: ")
    try:
        return float(teks)
    except ValueError:
        raise ValueError(f"{label} harus berupa angka.")

def main():
    print("=== SISTEM PENILAIAN ===")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")

    while True:
        try:
            nilai_tugas = baca_angka("Masukkan Nilai Tugas")
            nilai_uts = baca_angka("Masukkan Nilai UTS")
            nilai_uas = baca_angka("Masukkan Nilai UAS")
            mahasiswa = PenilaianMahasiswa(nama, nim, nilai_tugas, nilai_uts, nilai_uas)
            break
        except ValueError as error:
            print(f"Input tidak valid: {error}. Silakan coba lagi.")
            print("Silahkan isi ulang ketiga nilai.")
            if nim.strip() == "" or nama.strip() == "":
                nim = input("Masukkan NIM: ")
                nama = input("Masukkan Nama: ")

    print()
    mahasiswa.cetak_hasil()

main()