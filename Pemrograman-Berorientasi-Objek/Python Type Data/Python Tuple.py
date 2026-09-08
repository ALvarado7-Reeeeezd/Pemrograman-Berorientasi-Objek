# 1. Cara Bikin Tuple (Biasa, Mixed, Nested)
empty_tuple = ()
numbers_tuple = (1, 2, 3)
mixed_tuple = (1, "Hello", 3.4)
nested_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Tuple Packing & Unpacking
packed_tuple = 3, 4.6, "dog"  # tanpa tanda kurung
a, b, c = packed_tuple  # unpacking ke variabel terpisah
print("Unpacked:", a, b, c)

# Jebakan Tuple 1 elemen (wajib pake koma)
single_str = "hello"  # ini string
single_tuple = ("hello",)  # ini tuple
print("Tipe data single_tuple:", type(single_tuple))
print()


# 2. Akses Elemen (Indexing, Negative, Slicing)
char_tuple = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print("Elemen pertama:", char_tuple[0])
print("Elemen terakhir:", char_tuple[-1])

# Nested indexing
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print("Sifat 'mouse' index 3:", n_tuple[0][3])  # 's'
print("Angka di list dalam tuple:", n_tuple[1][1])  # 4

# Slicing [start:stop]
print("Slice [1:4]:", char_tuple[1:4])
print("Slice awal-2:", char_tuple[:-7])
print("Slice 8-akhir:", char_tuple[7:])
print()


# 3. Immutability (Sifat Gak Bisa Diubah)
my_tuple = (4, 2, 3, [6, 5])

# my_tuple[1] = 9  --> Error! Elemen tuple gak bisa diganti langsung

# TAPI kalau elemennya berupa list (mutable), isinya BISA diubah:
my_tuple[3][0] = 9
print("Tuple setelah list di dalamnya diubah:", my_tuple)

# Concatenation (+) & Repetition (*) -> menghasilkan tuple baru
tuple1 = (1, 2, 3) + (4, 5, 6)
tuple2 = ("Repeat",) * 3
print("Gabungan:", tuple1)
print("Pengulangan:", tuple2)

# del my_tuple[0]  --> Error! Gak bisa hapus item individu
# del my_tuple     --> Ini baru bisa (menghapus seluruh tuple dari memori)
print()


# 4. Method bawaan Tuple
letters = ("a", "p", "p", "l", "e")

print("Jumlah 'p':", letters.count("p"))
print("Index pertama 'l':", letters.index("l"))
print()


# 5. Keanggotaan (in), Looping & Fungsi Bawaan
print("Ada 'a' di tuple?", "a" in letters)
print("Gak ada 'b' di tuple?", "b" not in letters)

print("--- Loop Tuple ---")
for name in ("John", "Kate"):
    print("Hello", name)

# Multi-fungsi bawaan
num_tuple = (10, 20, 5, 30)
print("Panjang tuple (len):", len(num_tuple))
print("Nilai terbesar (max):", max(num_tuple))
print("Nilai terkecil (min):", min(num_tuple))
print("Total jumlah (sum):", sum(num_tuple))
print("Hasil sorted (dapetnya List):", sorted(num_tuple))

# Convert list ke tuple
list_data = [1, 2, 3]
converted_tuple = tuple(list_data)
print("Hasil konversi:", converted_tuple)