# Studi Kasus 1: Analisis Nilai Mahasiswa

# Data mahasiswa
data_mahasiswa = [
    {"nama": "Fandi", "nim": "2595114018", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Gilang", "nim": "2595114019", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Fuad", "nim": "2595114020", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Bima", "nim": "2595114021", "tugas": 78, "uts": 88, "uas": 84},
    {"nama": "Syahrul", "nim": "2595114022", "tugas": 88, "uts": 79, "uas": 90},
]

# Hitung nilai akhir menggunakan List Comprehension.
# Bobot: tugas 30%, UTS 30%, dan UAS 40%.
data_dengan_nilai = [
    {
        "nama": mahasiswa["nama"],
        "nim": mahasiswa["nim"],
        "tugas": mahasiswa["tugas"],
        "uts": mahasiswa["uts"],
        "uas": mahasiswa["uas"],
        "nilai_akhir": round(
            mahasiswa["tugas"] * 0.30
            + mahasiswa["uts"] * 0.30
            + mahasiswa["uas"] * 0.40,
            2,
        ),
    }
    for mahasiswa in data_mahasiswa
]

# Filter mahasiswa yang nilai akhirnya di atas 80.
mahasiswa_berprestasi = [
    mahasiswa
    for mahasiswa in data_dengan_nilai
    if mahasiswa["nilai_akhir"] > 80
]

# Urutkan mahasiswa dari nilai tertinggi ke terendah.
peringkat_mahasiswa = sorted(
    data_dengan_nilai,
    key=lambda mahasiswa: mahasiswa["nilai_akhir"],
    reverse=True,
)

print("=" * 72)
print("                  ANALISIS NILAI MAHASISWA")
print("=" * 72)
print("Bobot: Tugas 30% | UTS 30% | UAS 40%")

# Menampilkan seluruh nilai mahasiswa.
print("\nDAFTAR NILAI AKHIR")
print("-" * 72)

for mahasiswa in data_dengan_nilai:
    print(
        f"{mahasiswa['nama']:<10} | "
        f"NIM: {mahasiswa['nim']} | "
        f"Tugas: {mahasiswa['tugas']:>3} | "
        f"UTS: {mahasiswa['uts']:>3} | "
        f"UAS: {mahasiswa['uas']:>3} | "
        f"Akhir: {mahasiswa['nilai_akhir']:>5.2f}"
    )

# Menampilkan mahasiswa dengan nilai akhir di atas 80.
print("\nMAHASISWA BERPRESTASI (NILAI AKHIR > 80)")
print("-" * 72)

if mahasiswa_berprestasi:
    for mahasiswa in mahasiswa_berprestasi:
        print(
            f"{mahasiswa['nama']} | "
            f"NIM: {mahasiswa['nim']} | "
            f"Nilai Akhir: {mahasiswa['nilai_akhir']:.2f}"
        )
else:
    print("Belum ada mahasiswa dengan nilai akhir di atas 80.")

# Menampilkan ranking seluruh mahasiswa.
print("\nRANKING MAHASISWA")
print("-" * 72)

for nomor, mahasiswa in enumerate(peringkat_mahasiswa, start=1):
    print(
        f"{nomor}. {mahasiswa['nama']:<10} | "
        f"NIM: {mahasiswa['nim']} | "
        f"Nilai: {mahasiswa['nilai_akhir']:.2f}"
    )

# Mengambil mahasiswa dengan peringkat pertama.
mahasiswa_terbaik = peringkat_mahasiswa[0]

print("\nMAHASISWA TERBAIK")
print("-" * 72)
print(f"Nama        : {mahasiswa_terbaik['nama']}")
print(f"NIM         : {mahasiswa_terbaik['nim']}")
print(f"Nilai Tugas : {mahasiswa_terbaik['tugas']}")
print(f"Nilai UTS   : {mahasiswa_terbaik['uts']}")
print(f"Nilai UAS   : {mahasiswa_terbaik['uas']}")
print(f"Nilai Akhir : {mahasiswa_terbaik['nilai_akhir']:.2f}")
print("=" * 72)