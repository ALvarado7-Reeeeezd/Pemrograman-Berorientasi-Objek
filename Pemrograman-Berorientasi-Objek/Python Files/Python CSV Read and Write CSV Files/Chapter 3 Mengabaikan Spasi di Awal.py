import csv

# 1. Buat file dummy dengan spasi setelah koma
with open('people_space.csv', 'w') as f:
    f.write("SN, Name, City\n1, John, Washington\n2, Eric, Los Angeles\n")

# 2. Baca dengan skipinitialspace=True
with open('people_space.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)