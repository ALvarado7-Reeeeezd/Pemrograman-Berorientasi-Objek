import math
import random

# 1. Tipe data numerik di Python (int, float, complex)
print("--- Tipe Data Numerik ---")
num1 = 5
num2 = 5.42
num3 = 8 + 2j

print(num1, "is of type", type(num1))
print(num2, "is of type", type(num2))
print(num3, "is of type", type(num3))
print()


# 2. Sistem basis angka (Binary, Octal, Hexadecimal)
print("--- Basis Angka ---")
print("Biner (0b1101011):", 0b1101011)  # output: 107
print("Hex + Biner (0xFB + 0b10):", 0xFB + 0b10)  # output: 253
print("Oktal (0o15):", 0o15)  # output: 13
print()


# 3. Konversi tipe data (Implicit & Explicit)
print("--- Konversi Tipe Data ---")
# Implicit (otomatis berubah jadi float pas ada operasi dengan float)
print("1 + 2.0 =", 1 + 2.0)

# Explicit (pake fungsi bawaan)
val1 = int(2.3)  # desimal langsung dipotong
val2 = int(-2.8)
val3 = float(5)
val4 = complex("3+5j")

print("int(2.3) ->", val1)
print("int(-2.8) ->", val2)
print("float(5) ->", val3)
print("complex('3+5j') ->", val4)
print()


# 4. Modul Random
print("--- Modul Random ---")
print("Random range 10-20:", random.randrange(10, 20))

items = ["a", "b", "c", "d", "e"]
print("Random choice:", random.choice(items))

random.shuffle(items)
print("List setelah di-shuffle:", items)

print("Float random (0.0 - 1.0):", random.random())
print()


# 5. Modul Math
print("--- Modul Math ---")
print("Nilai Pi:", math.pi)
print("Cos(Pi):", math.cos(math.pi))
print("e^10 (exp):", math.exp(10))
print("Log10(1000):", math.log10(1000))
print("Sinh(1):", math.sinh(1))
print("Factorial(6):", math.factorial(6))