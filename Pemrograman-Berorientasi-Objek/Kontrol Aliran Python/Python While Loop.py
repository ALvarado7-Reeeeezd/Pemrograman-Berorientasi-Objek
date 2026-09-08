# 1. Contoh infinite loop (sengaja dicomment biar program nggak hang pas di-run)
"""
number = float(input("Enter a number: "))
while number >= 0.0:
    print(number)  # bakal jalan terus tanpa henti
"""


# 2. While loop dengan kondisi berhenti (finite)
number = float(input("Enter a number: "))

while number >= 0.0:
    print(number)
    # minta input lagi biar kondisinya bisa berubah
    number = float(input("Enter another number: "))

print()


# 3. Cek indentasi (print luar loop cuma jalan pas loop selesai)
task = input("Task: ")

while task != "q":
    print("Task done!")
    task = input("Task: ")

print("All tasks completed\n")


# 4. Cetak angka 1 sampai n
n = 10
i = 1

while i <= n:
    print(i)
    i += 1

print()


# 5. Ngitung total angka sampai user ngetik 0
total = 0
n = float(input("Enter a number (0 to stop): "))

while n != 0.0:
    total += n
    n = float(input("Enter a number (0 to stop): "))

print(f"Sum: {total}\n")


# 6. Contoh break (pake while True buat nunggu input 0)
while True:
    num = int(input("Enter a number (0 to quit): "))
    if num == 0:
        break
    print(num)

print()


# 7. Contoh continue (buat ngelewati angka ganjil)
i = 0

while i <= 10:
    i += 1
    if i % 2 != 0:
        continue  # skip print kalo ganjil
    print(i)

print()


# 8. While pake else (sistem input PIN)
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == "1212":
        print("Access granted.")
        break  # kelak kena break, blok else gak bakal diproses

    attempts -= 1
    print(f"Wrong PIN. {attempts} tries left.")
else:
    print("Account locked. Too many failed attempts.")