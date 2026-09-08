# 1. Bikin String Biasa & Multiline
model = "ChatGPT"
single_quote = 'Opus'

multiline_msg = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print("Single quote:", single_quote)
print("Multiline:\n", multiline_msg)
print()


# 2. Akses Karakter (Indexing, Negative Indexing, & Slicing)
print("Karakter pertama [0]:", model[0])       # C
print("Karakter kelima [4]:", model[4])        # G
print("Karakter terakhir [-1]:", model[-1])     # T
print("Karakter ke-4 dr belakang [-4]:", model[-4]) # t

# Slicing [start:stop]
print("Slice [0:4]:", model[0:4])  # Chat
print()


# 3. String Immutability (Gak Bisa Diganti Langsung)
# model[0] = 'W'  --> Error! Tipe str gak dukung item assignment

# Solusinya: bikin string baru lewat penggabungan (concatenation)
name = "Opus"
version = "5"
updated_name = name + " " + version
print("String baru hasil gabungan:", updated_name)
print()


# 4. Escape Sequences & String Formatting (f-string)
# Pake backslash (\) biar tanda kutip gak bikin syntax error
quote_msg = "He said, \"What's there?\""
print("Escape quote:", quote_msg)

# f-string buat gabungin variabel ke string dengan rapi
company = "Google"
field = "AI"
info = f"{company} is an {field} company."
print("f-string output:", info)
print()


# 5. Method Bawaan, Cek Keanggotaan, Looping, & Panjang String
text = "ChatGPT is great."
new_text = text.replace("ChatGPT", "Claude")
print("Setelah replace:", new_text)

# Cek substring pake 'in' dan 'not in'
print("Ada 'Chat' di model?", "Chat" in model)
print("Gak ada 'Claude' di model?", "Claude" not in model)

# Hitung panjang string
print("Panjang string model:", len(model))

# Looping tiap karakter
print("--- Loop Karakter ---")
for c in "Opus":
    print(c)