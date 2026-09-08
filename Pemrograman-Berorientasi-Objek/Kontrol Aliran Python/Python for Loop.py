# 1. Loop dasar lewat list
models = ["Fable", "ChatGPT", "Gemini"]

for model in models:
    print(model)
    print("---")


# 2. Cek indentasi (print luar loop cuma jalan sekali)
numbers = [1, 2, 3]

for num in numbers:
    print(f"Processing: {num}")
    print(f"Done with: {num}")

print("All done\n")


# 3. Pake range() buat perulangan angka
# range(1, 11) itu dari 1 sampe 10
for i in range(1, 11):
    print(f"Displaying product {i}")
print()


# 4. Ngeloop isi string karakter per karakter
language = "Python"

for x in language:
    print(x)
print()


# 5. Contoh break (langsung keluar dari loop)
print("--- Contoh Break ---")
for num in range(1, 11):
    if num == 3:
        break
    print(num)  # cuma ngeprint 1 sama 2
print()


# 6. Contoh continue (ngelewati iterasi yang sekarang)
print("--- Contoh Continue ---")
for num in range(1, 6):
    if num == 3:
        continue
    print(num)  # angka 3 dilewati
print()


# 7. For pake else (jalan pas loop kelar, tapi gak jalan kalo kena break)
stock = ["Laptop", "Keyboard", "Mouse"]
order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")
print()


# 8. Pake underscore (_) kalo gak butuh nilai variabel loop-nya
for _ in range(0, 4):
    print("Hi")
print()


# 9. Ngitung total jumlah angka (1 sampe 10)
total = 0

for i in range(1, 11):
    total += i

print(f"Total = {total}\n")


# 10. Nested loop (loop di dalem loop)
attributes = ["Electric", "Fast"]
cars = ["Tesla", "Porsche", "Mercedes"]

for attribute in attributes:
    for car in cars:
        print(attribute, car)
    print("-----")