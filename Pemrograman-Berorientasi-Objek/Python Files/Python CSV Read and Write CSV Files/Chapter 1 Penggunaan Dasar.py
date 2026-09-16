import csv

# 1. Buat file dummy 'innovators.csv' otomatis
with open('innovators.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['SN', 'Name', 'Contribution'])
    writer.writerow(['1', 'Linus Torvalds', 'Linux Kernel'])
    writer.writerow(['2', 'Tim Berners-Lee', 'World Wide Web'])
    writer.writerow(['3', 'Guido van Rossum', 'Python Programming'])

# 2. Baca file
with open('innovators.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)