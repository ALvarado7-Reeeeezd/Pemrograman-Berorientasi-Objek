# 1. Break di dalam for loop
print("--- Break di For Loop ---")
number = int(input("Enter a number: "))

for i in range(1, 6):
    if i == number:
        break  # berhenti kalo nilainya sama dengan input
    print(i)
print()


# 2. Break di dalam while loop (pake while True)
print("--- Break di While Loop ---")
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break  # keluar kalo dapet angka negatif
    print(f"You entered {number}")
print()


# 3. Continue di dalam for loop (skip angka genap)
print("--- Continue di For Loop ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # skip print kalo genap
    print(i)
print()


# 4. Gabungan continue dan break (jumlahin angka positif)
print("--- Sum Positive Numbers ---")
total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number < 0:
        continue  # skip angka negatif

    if number == 0:
        break  # stop loop kalo dapet 0

    total += number

print(f"Sum of positive numbers: {total}\n")


# 5. Loop pake klausul else
print("--- Loop dengan Else ---")
stock = ["Laptop", "Keyboard", "Mouse"]
order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")