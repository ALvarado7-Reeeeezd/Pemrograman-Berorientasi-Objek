# nyoba if doang
age = int(input("Enter your age: "))

if age >= 18:
    print("Grant access to the website.")
    print("Show products.")
print("Program complete.\n")


# simulasi login pake if...else
username_db = "admin"
password_db = "iyeng"

username = input("Enter username: ")
password = input("Enter password: ") 

if username == username_db and password == password_db:
    print("Welcome back.")
else:
    print("Access denied.")
print()


# cek umur pake elif buat milih beberapa kondisi
age = int(input("Enter your age again: "))

if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("Grant access.")
else:
    print("Deny access.")


# contoh nested if (if di dalem if) 
# agak ribet bacanya, tapi bisa
if age < 18:
    if age < 0:
        print("Invalid age.")
    else:
        print("Deny access.")
else:
    print("Grant access.")


# shorthand if...else (bisa sebaris aja)
status = "Adult" if age >= 18 else "Minor"
print("Status:", status, "\n")


# program nyari angka paling gede dari 3 inputan
print("--- Cari Angka Terbesar ---")
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3

print("The largest number is:", largest)