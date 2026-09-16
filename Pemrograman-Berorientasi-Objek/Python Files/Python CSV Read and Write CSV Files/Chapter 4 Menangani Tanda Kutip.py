import csv

# 1. Buat file dummy bertanda kutip
with open('quotes.csv', 'w') as f:
    f.write('"SN", "Name", "Quotes"\n1, Buddha, "What we think we become"\n')

# 2. Baca menggunakan QUOTE_ALL
with open('quotes.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)