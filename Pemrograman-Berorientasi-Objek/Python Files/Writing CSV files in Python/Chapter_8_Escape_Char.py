# Judul: Writing CSV - Using Escape Character
# Penjelasan: Untuk menyisipkan karakter escape (misal: '/') pada teks yang mengandung tanda kutip/koma saat fitur quoting dimatikan (QUOTE_NONE).

import csv

row_list = [
    ['Book', 'Quote'],
    ['Lord of the Rings',
        '"All we have to decide is what to do with the time that is given us."'],
    ['Harry Potter', '"It matters not what someone is born, but what they grow to be."']
]

with open('book.csv', 'w', newline='') as file:
    writer = csv.writer(file, escapechar='/', quoting=csv.QUOTE_NONE)
    writer.writerows(row_list)
