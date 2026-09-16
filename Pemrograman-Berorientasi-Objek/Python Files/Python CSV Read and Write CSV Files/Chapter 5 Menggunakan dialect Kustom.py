import csv

# 1. Buat file dummy dengan format campuran (| dan kutip)
with open('office.csv', 'w') as f:
    f.write('"ID"| "Name"| "Email"\n"A878"| "Alfonso K. Hamby"| "alfonso@mail.com"\n')

# 2. Registrasi Dialect
csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

# 3. Baca menggunakan Dialect
with open('office.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)