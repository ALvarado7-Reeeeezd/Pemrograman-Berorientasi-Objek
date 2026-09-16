import csv

# 1. Buat file dummy
with open('people_dict.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'Profession'])
    writer.writerow(['Jack', '23', 'Doctor'])
    writer.writerow(['Miller', '22', 'Engineer'])

# 2. Baca sebagai Dictionary
with open("people_dict.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))