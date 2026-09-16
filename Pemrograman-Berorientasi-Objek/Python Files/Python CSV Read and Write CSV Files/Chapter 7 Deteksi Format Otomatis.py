import csv

# 1. Buat file dummy
with open('office_sniff.csv', 'w') as f:
    f.write('"ID"| "Name"| "Email"\nA878| "Alfonso K. Hamby"| "alfonso@mail.com"\n')

# 2. Deteksi format file (Sniffing)
with open('office_sniff.csv', 'r') as csvfile:
    sample = csvfile.read(64)
    has_header = csv.Sniffer().has_header(sample)
    print("Memiliki Header:", has_header)

    deduced_dialect = csv.Sniffer().sniff(sample)

# 3. Baca kembali menggunakan dialect hasil deteksi
with open('office_sniff.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, deduced_dialect)
    for row in reader:
        print(row)