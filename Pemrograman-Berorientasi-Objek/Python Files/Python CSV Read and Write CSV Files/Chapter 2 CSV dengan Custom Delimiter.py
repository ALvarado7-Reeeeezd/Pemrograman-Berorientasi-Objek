import csv

# 1. Buat file dummy dengan pemisah Tab
with open('innovators_tab.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['SN', 'Name', 'Contribution'])
    writer.writerow(['1', 'Linus Torvalds', 'Linux Kernel'])
    writer.writerow(['2', 'Tim Berners-Lee', 'World Wide Web'])

# 2. Baca file dengan delimiter Tab
with open('innovators_tab.csv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)