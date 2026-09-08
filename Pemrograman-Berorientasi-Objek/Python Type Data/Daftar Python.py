# 1. Cara Bikin List
cart = ["T-shirt", "Lamp", "Pen"]
my_list = [1, "Python", 3.14]
empty_list = []

# Bikin list dari iterable pake list()
vowels = "aeiou"
vowels_list = list(vowels)
print("Vowels list:", vowels_list)
print()


# 2. Akses Item pake Positif & Negatif Indexing
languages = ["Python", "Swift", "C++"]
print(f"languages[0] = {languages[0]}")
print(f"languages[2] = {languages[2]}")

print("languages[-1] =", languages[-1])  # item terakhir
print("languages[-3] =", languages[-3])  # item pertama dari belakang
print()


# 3. Ubah dan Tambah Item
cart = ["T-shirt", "Lamp", "Pen"]

# Ubah isi berdasarkan indeks
cart[1] = "Shoes"

# Tambah 1 item di paling belakang
cart.append("Book")

# Tambah banyak item sekaligus
fav_items = ["Headphones", "Phone"]
cart.extend(fav_items)

# Sisip item di indeks tertentu (misal indeks 2)
cart.insert(2, "Watch")
print("Cart setelah di-update:", cart)
print()


# 4. Hapus Item dari List
cart = ["T-shirt", "Shoes", "Watch", "Pen", "Book"]

cart.remove("Pen")  # hapus berdasarkan nilai
last_item = cart.pop()  # hapus & ambil item terakhir
print("Item yang di-pop:", last_item)

del cart[1]  # hapus berdasarkan indeks
print("Cart setelah hapus-hapus:", cart)

cart.clear()  # kosongin semua isi list
print("Cart bersih:", cart)
print()


# 5. Copy List yang Bener (Shallow Copy)
favorite_items = ["T-shirt", "Lamp", "Pen"]

# Jangan pake = langsung (karena cuma nge-refer ke memori yang sama)
# Pake .copy() biar bikin list baru yang independen
cart = favorite_items.copy()
favorite_items.append("Book")

print("favorite_items:", favorite_items)
print("cart (hasil copy):", cart)
print()


# 6. Method bawaan, Panjang List, Cek Keanggotaan & Loop
numbers = [4, 2, 9, 1, 2]

numbers.sort()  # urutin dari kecil ke gede
print("Sorted:", numbers)

numbers.reverse()  # balik urutan
print("Reversed:", numbers)

print("Jumlah angka 2:", numbers.count(2))
print("Indeks angka 9:", numbers.index(9))
print("Panjang list:", len(numbers))

# Cek apakah item ada di list (in)
print("Ada Lamp di cart?", "Lamp" in favorite_items)
print("Ada Book di cart?", "Book" in cart)
print()

# Iterasi/looping lewat isi list
print("--- Loop Isi List ---")
for item in favorite_items:
    print("-", item)