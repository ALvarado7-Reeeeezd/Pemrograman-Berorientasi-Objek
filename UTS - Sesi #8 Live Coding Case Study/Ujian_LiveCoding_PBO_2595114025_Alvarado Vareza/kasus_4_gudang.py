class Barang:
    """Satu jenis barang beserta stoknya."""
    def __init__(self, nama, stok):
        if nama.strip() == "":
            raise ValueError("Nama barang tidak boleh kosong.")
        self.nama = nama
        self.stok = self.validasi_stok(stok)

    def validasi_stok(self, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif.")
        return stok

    def tentukan_status(self):
        if self.stok < 5:
            return "KRITIS"
        elif self.stok <= 10:
            return "MENIPIS"
        else:
            return "AMAN"

class InventarisGudang:
    """Menyimpan banyak objek Barang dalam sebuah list"""

    def __init__(self):
        self.daftar_barang = []

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)

    def hitung_total_unit(self):
        total =  0
        for barang in self.daftar_barang:
            total += barang.stok
        return total

    def rekap_status(self):
        """Mengembalikan jumlah barang KRITIS, MENIPIS, dan AMAN (berurutan)"""
        kritis = 0
        menipis = 0
        aman = 0
        for barang in self.daftar_barang:
            status = barang.tentukan_status()
            if status == "KRITIS":
                kritis += 1
            elif status == "MENIPIS":
                menipis += 1
            else:
                aman += 1
        return kritis, menipis, aman

    def tampilkan_laporan(self):
        print("=== LAPORAN STOK ===")
        for nomor, barang in enumerate(self.daftar_barang, start=1):
            print(f"{nomor}. {barang.nama}")
            print(f"   Stok: {barang.stok}")
            print(f"   Status: {barang.tentukan_status()}")

        kritis, menipis, aman =self.rekap_status()
        print("=== REKAPITULASI ===")
        print(f"Total jenis barang : {len(self.daftar_barang)}")
        print(f"Total unit barang   : {self.hitung_total_unit()}")
        print(f"Jumlah barang KRITIS : {kritis}")
        print(f"Jumlah barang MENIPIS : {menipis}")
        print(f"Jumlah barang AMAN : {aman}")
        print("=====================")


def baca_bilangan_bulat(label):
    """Membaca input bilangan bulat; kalau bukan, lempar Value Error dengan pesan jelas."""
    teks = input(f"{label}:")
    try:
        return int(teks)
    except ValueError:
        raise ValueError(f"Input untuk {label} harus berupa bilangan bulat.")


def baca_jumlah_jenis():
    """Jumlah jenis barang harus bilangan bulat positif."""
    while True:
        try:
            jumlah = baca_bilangan_bulat("Jumlah jenis barang")
            if jumlah <= 0:
                raise ValueError("Jumlah jenis barang harus bilangan bulat positif.")
            return jumlah
        except ValueError as error:
            print(f"Input tidak valid: {error}")


def main():
    print("=== DATA STOK GUDANG ===")
    jumlah_jenis = baca_jumlah_jenis()
    gudang = InventarisGudang()

    for i in range(1, jumlah_jenis + 1):
        print(f"Barang ke-{i}")
        while True:
            try:
                nama = input("Nama barang:")
                stok = baca_bilangan_bulat("Jumlah stok")
                barang = Barang(nama, stok)
                break
            except ValueError as error:
                print(f"Input tidak valid: {error}")
                print("Silahkan isi ulang data barang ini.")
        gudang.tambah_barang(barang)

    print()
    gudang.tampilkan_laporan()



main()