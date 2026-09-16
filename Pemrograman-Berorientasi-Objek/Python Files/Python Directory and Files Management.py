import os

# Mendapatkan direktori kerja saat ini
print(os.getcwd())# Output: C:\Program Files\PyScripter

# Mengubah direktori kerja
# os.chdir('C:\\Python33')  # Di-comment agar tidak terjadi FileNotFoundError pada sistem Anda
print(os.getcwd())

print(os.getcwd())

# Menampilkan semua isi sub-direktori dan file
os.listdir()

# os.listdir('G:\\')  # Di-comment jika drive G:\ tidak tersedia pada perangkat Anda

# Membuat direktori baru bernama 'test'
# os.mkdir('test')  # Di-comment agar tidak membuat folder berulang jika dijalankan kembali

os.listdir()

# Mengubah nama direktori dari 'test' menjadi 'new_one'
# os.rename('test','new_one')  # Di-comment agar tidak error jika folder 'test' belum ada

os.listdir()

# Menghapus file 'myfile.txt'
# os.remove("myfile.txt")  # Di-comment agar tidak memicu FileNotFoundError

# Menghapus direktori kosong 'mydir'
# os.rmdir("mydir")  # Di-comment agar tidak memicu FileNotFoundError

import shutil
# Menghapus direktori 'mydir' beserta seluruh isinya
# shutil.rmtree("mydir")  # Di-comment demi keamanan file sistem Anda