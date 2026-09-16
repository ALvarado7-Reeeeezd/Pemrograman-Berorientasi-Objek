# Judul: Writing CSV - Custom Dialect
# Penjelasan: Untuk mengelompokkan aturan/format penulisan CSV (delimiter & quoting) ke dalam satu Dialect kustom agar modular dan bisa dipakai berulang.

import csv

row_list = [
    ["ID", "Name", "Email"],
    ["A878", "Alfonso K. Hamby", "alfonsokhamby@rhyta.com"],
    ["F854", "Susanne Briard", "susannebriard@armyspy.com"],
    ["E833", "Katja Mauer", "kmauer@jadoop.com"]
]

csv.register_dialect('myDialect',
                     delimiter='|',
                     quoting=csv.QUOTE_ALL)

with open('office.csv', 'w', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerows(row_list)
