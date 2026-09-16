# Pengimporan modul dengan nama jalur lengkap (full namespace)
# import Game.Level.start  # Di-comment agar tidak terjadi ModuleNotFoundError

# Memanggil fungsi menggunakan nama lengkap paket & modul
# Game.Level.start.select_difficulty(2)

# Pengimporan modul tanpa awalan paket
# from Game.Level import start

# Memanggil fungsi langsung melalui nama modul
# start.select_difficulty(2)

# Hanya mengimpor fungsi spesifik yang dibutuhkan
# from Game.Level.start import select_difficulty

# Memanggil fungsi secara langsung
# select_difficulty(2)