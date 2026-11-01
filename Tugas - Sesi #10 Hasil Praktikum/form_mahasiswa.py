import tkinter as tk
from tkinter import ttk, messagebox # messagebox ditambahin buat bikin pop-up validasi error

# 1. Setup Jendela Utama
root = tk.Tk()
root.title("Form Identitas Mahasiswa")
# Ukuran diperbesar sedikit biar muat buat input alamat
root.geometry("450x450") 

# 2. Menentukan Tema Warna (Kombinasi Warna Konsisten)
bg_main = "#f4f6f9"  # Warna background (abu-abu kebiruan terang)
txt_color = "#333333" # Warna teks (abu-abu gelap)
btn_simpan = "#007bff" # Biru
btn_reset = "#ffc107"  # Kuning/Orange
btn_keluar = "#dc3545" # Merah

root.configure(bg=bg_main) # Terapin warna background ke jendela utama

# 3. Judul (Menggunakan grid)
tk.Label(
    root, text="FORM IDENTITAS MAHASISWA", 
    font=("Arial", 14, "bold"), bg=bg_main, fg=txt_color
).grid(row=0, column=0, columnspan=2, pady=15)

# 4. Label dan Input NAMA
tk.Label(root, text="Nama", bg=bg_main, font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=20, pady=5)
nama = tk.Entry(root, width=35)
nama.grid(row=1, column=1, pady=5, sticky="w")

# 5. Label dan Input NIM
tk.Label(root, text="NIM", bg=bg_main, font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=20, pady=5)
nim = tk.Entry(root, width=35)
nim.grid(row=2, column=1, pady=5, sticky="w")

# 6. Label dan Input PROGRAM STUDI (Combobox)
tk.Label(root, text="Program Studi", bg=bg_main, font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=20, pady=5)
prodi = ttk.Combobox(root, values=["Teknik Informatika", "Sistem Informasi", "Teknologi Informasi"], state="readonly", width=32)
prodi.grid(row=3, column=1, pady=5, sticky="w")

# 7. Label dan Input ALAMAT (Tugas 1: Widget Text)
tk.Label(root, text="Alamat", bg=bg_main, font=("Arial", 10)).grid(row=4, column=0, sticky="nw", padx=20, pady=5)
alamat = tk.Text(root, width=26, height=4, font=("Arial", 10))
alamat.grid(row=4, column=1, pady=5, sticky="w")

# 8. Label untuk Hasil
hasil = tk.Label(root, text="", bg=bg_main, fg=txt_color, justify="left", font=("Arial", 10))
hasil.grid(row=6, column=0, columnspan=2, pady=10)

# 9. Fungsi Tombol Simpan (Tugas 3: Validasi Kosong)
def simpan():
    # Ambil data dari semua input (.strip() buat ngilangin spasi kosong di awal/akhir)
    val_nama = nama.get().strip()
    val_nim = nim.get().strip()
    val_prodi = prodi.get()
    # Mengambil teks dari Text widget (dari baris 1 karakter 0, sampai akhir)
    val_alamat = alamat.get("1.0", tk.END).strip()

    # Validasi: Cek kalau Nama atau NIM kosong
    if val_nama == "" or val_nim == "":
        messagebox.showwarning("Peringatan", "Nama dan NIM tidak boleh kosong!")
        return # Menghentikan fungsi biar hasil nggak ditampilin

    # Kalau validasi lolos, tampilkan hasilnya
    hasil.config(
        text=f"--- Hasil Input ---\nNama: {val_nama}\nNIM: {val_nim}\nProdi: {val_prodi}\nAlamat: {val_alamat}"
    )

# 10. Fungsi Tombol Reset
def reset():
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END) # Cara hapus Text widget
    hasil.config(text="")

# 11. Fungsi Tombol Keluar (Tugas 5)
def keluar():
    root.destroy() # Perintah bawaan Tkinter buat nutup jendela

# 12. Frame khusus buat naruh jejeran Tombol (Tugas 4: Atur ulang layout)
frame_tombol = tk.Frame(root, bg=bg_main)
frame_tombol.grid(row=5, column=0, columnspan=2, pady=15)

# Bikin 3 tombol di dalam frame_tombol (Tugas 2: Modif warna)
tk.Button(frame_tombol, text="Simpan", command=simpan, bg=btn_simpan, fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(frame_tombol, text="Reset", command=reset, bg=btn_reset, fg="black", width=10).grid(row=0, column=1, padx=5)
tk.Button(frame_tombol, text="Keluar", command=keluar, bg=btn_keluar, fg="white", width=10).grid(row=0, column=2, padx=5)

# 13. Jalankan Aplikasi
root.mainloop()