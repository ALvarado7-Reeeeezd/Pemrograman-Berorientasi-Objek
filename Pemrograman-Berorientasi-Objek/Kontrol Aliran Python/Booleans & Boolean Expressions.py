# 1. Tipe Data Boolean dasar
is_valid = False    # boolean asli
is_valid_str = "False"  # ini cuma string
# is_valid_err = false  # error! harus pake F kapital


# 2. Operator Perbandingan (< dan <=)
print("--- Perbandingan < dan <= ---")
x = 10
y = 20

print(f"x < y  ---> {x < y}")      # True
print(f"x <= y ---> {x <= y}")     # True
print(f"x < 10 ---> {x < 10}")     # False (10 gak kurang dari 10)
print(f"x <= 10 ---> {x <= 10}")   # True (karena ada 'sama dengan'-nya)
print()


# 3. Operator Perbandingan (> dan >=)
print("--- Perbandingan > dan >= ---")
print(f"x > y  ---> {x > y}")      # False
print(f"x >= y ---> {x >= y}")     # False
print(f"x > 10 ---> {x > 10}")     # False
print(f"x >= 10 ---> {x >= 10}")   # True
print()


# 4. Operator Perbandingan (== dan !=)
print("--- Perbandingan == dan != ---")
print(f"x == y  ---> {x == y}")    # False
print(f"x != y  ---> {x != y}")    # True
print(f"x == 10 ---> {x == 10}")   # True
print(f"x != 10 ---> {x != 10}")   # False

# Cek perbandingan string (case sensitive)
name1 = "Alice"
print(name1 == "Alice")  # True
print(name1 == "alice")  # False
print(name1 != "Alice")  # False
print(name1 != "alice")  # True
print()


# 5. Logical Operators (and, or, not)
print("--- Operator Logika ---")
age = 20
citizen = "yes"

# AND: dua-duanya harus True
is_voter = (age >= 18) and (citizen == "yes")
print("Bisa nyoblos (AND)?", is_voter)

# OR: salah satu True aja udah beres
is_eligible = (age >= 18) or (citizen == "yes")
print("Memenuhi syarat (OR)?", is_eligible)

# NOT: pembalikan nilai
passcode = "1345"
entered_code = "1345"
print("Passcode cocok?", passcode == entered_code)
print("Passcode GAK cocok?", not (passcode == entered_code))
print()


# 6. Fungsi bool() (Truthy vs Falsy)
print("--- Truthy & Falsy ---")
print("0:", bool(0))             # False (angka 0 itu falsy)
print("12:", bool(12))           # True
print("String 'Python':", bool("Python"))  # True
print("String 'False':", bool("False"))   # True! (soalnya string-nya gak kosong)
print("String kosong '':", bool(""))      # False