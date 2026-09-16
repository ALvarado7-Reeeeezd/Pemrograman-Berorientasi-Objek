import math
import random

# 1. Deklarasi dan Pemanggilan Fungsi Dasar
print("--- Fungsi Dasar ---")
def greet():
    print('Hello World!')

# Memanggil fungsi greet
greet()
print('Outside function')
print()


# 2. Fungsi dengan Argumen/Parameter
print("--- Fungsi dengan Argumen ---")
def greet_person(name):
    print("Hello", name)

greet_person("John")
greet_person("David")

def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

add_numbers(5, 4)
print()


# 3. Fungsi dengan Return Value
print("--- Fungsi dengan Return Value ---")
def find_square(num):
    result = num * num
    return result

square = find_square(3)
print('Square:', square)
print()


# 4. Penggunaan pass Statement (Placeholder)
print("--- Pass Statement ---")
def future_function():
    pass

# Menjalankan fungsi tanpa aksi/error
future_function()
print("Fungsi pass berhasil dijalankan tanpa error.")
print()


# 5. Modul Math (Library Functions)
print("--- Modul Math ---")
# sqrt menghitung akar kuadrat
square_root = math.sqrt(4)
print("Square Root of 4 is", square_root)

# pow menghitung pemangkatan
power = pow(2, 3)
print("2 to the power 3 is", power)

# 6. Modul Random (Library Functions)
print("--- Modul Random ---")
# randint menghasilkan bilangan acak dalam rentang tertentu
random_number = random.randint(1, 10)
print("Random number between 1 and 10 is", random_number)

def greet(name, message="Hello"):
    print(message, name)# memanggil fungsi dengan kedua argumen
greet("Alice", "Good Morning")# memanggil fungsi hanya dengan satu argumen
greet("Bob")

# fungsi untuk menjumlahkan berapa pun jumlah argumennya
def add_all(*numbers):
    return sum(numbers)# meneruskan berapa pun jumlah argumennya
print(add_all(1, 2, 3, 4))   

# fungsi untuk mencetak argumen kata kunci (keyword arguments)
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")# meneruskan berapa pun jumlah argumen kata kunci
greet(name="John", greeting="Hello")