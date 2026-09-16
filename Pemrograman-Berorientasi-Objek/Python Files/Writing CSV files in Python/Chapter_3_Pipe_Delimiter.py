# Judul: Writing CSV - Pipe Delimiter
# Penjelasan: Untuk membuat file CSV dengan pemisah kolom selain koma, yaitu karakter Pipe ('|').

import csv

data_list = [
    ["SN", "Name", "Contribution"],
    [1, "Linus Torvalds", "Linux Kernel"],
    [2, "Tim Berners-Lee", "World Wide Web"],
    [3, "Guido van Rossum", "Python Programming"]
]

with open('innovators_pipe.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)
