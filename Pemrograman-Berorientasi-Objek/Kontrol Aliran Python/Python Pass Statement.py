# 1. Contoh penggunaan pass di dalam if-else
# Bermanfaat pas mau bikin struktur dulu tapi belum ada isinya
is_valid = True

if is_valid:
    pass  # belum tau mau diisi apa, yang penting gak error
else:
    print("Login invalid. Redirect to form.")


# 2. Contoh pass di dalam fungsi (function placeholder)
def calculate_token():
    pass  # logika perhitungan token bakal ditulis nanti


# 3. Alternatif pass pake Ellipsis (...)
# Bisa dipake juga tapi standar industri tetep pake pass
def calculate_token_alt():
    ...


# 4. Contoh pass di dalam loop
for i in range(1, 5):
    if i == 3:
        pass  # lewati tanpa melakukan apa-apa
    else:
        print(f"Angka: {i}")