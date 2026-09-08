# 1. Cara Bikin Set & Otomatis Hapus Duplikat
student_id = {112, 114, 116, 118, 115}
vowel_letters = {"a", "e", "i", "o", "u"}
mixed_set = {"Hello", 101, -2, "Bye"}

# Otomatis ngilangin duplikat
numbers = {2, 4, 6, 6, 2, 8}
print("Set tanpa duplikat:", numbers)

# Hati-hati pas bikin set kosong!
empty_set = set()  # set kosong (bener)
empty_dict = {}  # ini bikin dictionary kosong
print("Tipe empty_set:", type(empty_set))
print()


# 2. Tambah & Update Isi Set
companies = {"Lacoste", "Ralph Lauren"}

# Tambah 1 elemen pake add()
companies.add("Puma")

# Tambah banyak elemen sekaligus (bisa dari list/tuple) pake update()
tech_companies = ["apple", "google", "apple"]
companies.update(tech_companies)
print("Companies setelah update:", companies)
print()


# 3. Hapus Elemen (discard vs remove vs pop)
languages = {"Swift", "Java", "Python"}

# discard() gak bakal error kalo elemennya gak ada
languages.discard("Java")
languages.discard("C++")  # tetep aman, gak error

# pop() ngambil & ngapus elemen secara acak
random_item = languages.pop()
print("Item yang ter-pop:", random_item)
print("Sisa languages:", languages)

languages.clear()  # kosongin semua isi set
print("Set kosong:", languages)
print()


# 4. Operasi Matematika Set (Union, Intersection, Difference, Sym Difference)
A = {1, 2, 3, 5}
B = {0, 2, 4, 6}

# Union (Gabungan) -> pake | atau union()
print("Union:", A | B)

# Intersection (Irisan) -> pake & atau intersection()
print("Intersection:", A & B)

# Difference (Selisih) -> pake - atau difference()
print("Difference (A - B):", A - B)

# Symmetric Difference (Bukan Irisan) -> pake ^ atau symmetric_difference()
print("Symmetric Difference:", A ^ B)
print()


# 5. Cek Kesamaan, Looping & Fungsi Bawaan
set_x = {1, 3, 5}
set_y = {3, 5, 1}

print("Apakah set_x == set_y?", set_x == set_y)  # True (urutan gak nengaruh)

print("--- Loop Isi Set ---")
fruits = {"Apple", "Peach", "Mango"}
for fruit in fruits:
    print("-", fruit)

# Beberapa fungsi bawaan
even_numbers = {2, 4, 6, 8}
print("Panjang set (len):", len(even_numbers))
print("Nilai terbesar (max):", max(even_numbers))
print("Hasil sorted (dapetnya List):", sorted(even_numbers))