
class Pegawai:
    def __init__(self, id_pegawai, nama):
        self.id_pegawai = id_pegawai
        self.nama = nama


class Gaji:
    def __init__(self, gaji):
        self.gaji = gaji


class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek


class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama)
        Gaji.__init__(self, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def tampilkan_data(self):
        print("ID Pegawai  :", self.id_pegawai)
        print("Nama        :", self.nama)
        print("Gaji        : Rp", self.gaji)
        print("Nama Proyek :", self.nama_proyek)


# Membuat object Project Manager
pm1 = ProjectManager(
    "PGAB001",
    "Fandi",
    8000000,
    "Pengembangan Aplikasi"
)

# Menampilkan data
print("=== DATA PROJECT MANAGER ===")
pm1.tampilkan_data()