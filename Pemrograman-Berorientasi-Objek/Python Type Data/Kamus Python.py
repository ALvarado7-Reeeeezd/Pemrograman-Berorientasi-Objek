# 1. Cara Bikin Dictionary (Key: Value)
# Key harus unik dan bersifat immutable (string, int, tuple)
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London",
}

# Bikin pake dict()
user_info = dict(name="Alex", age=25)
print("Country capitals:", country_capitals)
print("User info:", user_info)
print()


# 2. Akses Elemen (Bracket vs .get())
print("Capital Germany:", country_capitals["Germany"])

# Pake .get() lebih aman karena gak bakal bikin error kalo key-nya gak ada
print("Capital Canada (.get):", country_capitals.get("Canada"))
print("Capital Japan (.get):", country_capitals.get("Japan"))  # dapet None
print("Capital Japan (default):", country_capitals.get("Japan", "N/A"))
print()


# 3. Ubah dan Tambah Elemen
# Tambah key baru
country_capitals["Italy"] = "Naples"

# Ubah nilai key yang udah ada
country_capitals["Italy"] = "Rome"

# Tambah / Ubah sekaligus banyak pake .update()
country_capitals.update({"Japan": "Tokyo", "England": "London"})
print("Updated capitals:", country_capitals)
print()


# 4. Hapus Elemen (del, .pop(), .popitem(), .clear())
# Hapus pake del
del country_capitals["Germany"]

# Hapus & dapet nilainya pake .pop()
removed_capital = country_capitals.pop("Canada")
print("Capital Canada yang di-pop:", removed_capital)

# Hapus item terakhir yang dimasukkan pake .popitem()
last_pair = country_capitals.popitem()
print("Pasangan terakhir yang dihapus:", last_pair)

# Copy dulu biar gak ngacak-ngacak data asli pas dikosongin
temp_dict = country_capitals.copy()
temp_dict.clear()  # kosongin semua isi dictionary
print("Temp dict setelah clear:", temp_dict)
print()


# 5. Iterasi / Looping lewat Dictionary
print("--- Loop Keys & Values ---")
# Looping key-nya aja
for country in country_capitals:
    print("Country:", country)

print()
# Looping nilainya (value)
for capital in country_capitals.values():
    print("Capital:", capital)

print()
# Looping key dan value barengan pake .items()
for country, capital in country_capitals.items():
    print(f"{country} -> {capital}")
print()


# 6. Cek Keanggotaan (in), Panjang Dict & Method Lainnya
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# Operator 'in' cuma meriksa Key, bukan Value
print("Ada .pdf?", ".pdf" in file_types)
print("Ada .mp3?", ".mp3" in file_types)
print("Gak ada .mp3?", ".mp3" not in file_types)

# Panjang dictionary
print("Panjang file_types:", len(file_types))

# Ambil semua keys atau values ke bentuk list-like object
print("Semua keys:", list(file_types.keys()))
print("Semua values:", list(file_types.values()))