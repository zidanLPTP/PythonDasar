# ===============================================
# Modul: read.py
# Topik: Membaca File Secara Aman di Python
# Cocok untuk: Pemula belajar file handling
# ===============================================

import os

# 📌 1. Menentukan path file secara dinamis
# -----------------------------------------------
# Tujuannya agar file tetap bisa dibaca meskipun folder dipindah
# __file__ -> merujuk ke lokasi file skrip Python ini
BASE_DIR = os.path.dirname(__file__)  # direktori file ini
file_path = os.path.join(BASE_DIR, "contoh_create.txt")  # gabungkan dengan nama file

with open(file_path, "a") as file:
    file.write("Text ini ditambahkan dari file read.py")
# 📌 2. Membuka dan membaca isi file dengan mode 'r+'
# -----------------------------------------------
# 'r+' = baca dan tulis (tanpa menghapus isi file)
# File harus sudah ada, jika tidak: FileNotFoundError
try:
    with open(file_path, "r+") as file:
        print("\n📄 === Membaca Isi File: contoh_create.txt ===")
        print(file.read())
except FileNotFoundError:
    print("❌ File tidak ditemukan! Pastikan file sudah dibuat.")
except Exception as e:
    print("⚠️ Terjadi kesalahan:", e)
else:
    print("✅ File berhasil dibaca.")
finally:
    print("📌 Proses membaca selesai.")

# 📌 3. Tabel Mode File
# -----------------------------------------------
tabel_mode = """
|-------|------------------------------------------------|
| Mode  | Deskripsi                                      |
|-------|------------------------------------------------|
| 'r'   | Read (baca), file harus sudah ada              |
| 'r+'  | Read & Write, file harus ada, tidak hapus isi  |
| 'rb'  | Read binary (untuk file seperti gambar, PDF)   |
| 'rb+' | Read & write binary                            |
|-------|------------------------------------------------|
"""
print("\n📖 TABEL MODE FILE YANG BISA DIGUNAKAN UNTUK MEMBACA")
print(tabel_mode)

# 📌 4. Menampilkan lokasi file yang sedang diakses
# -----------------------------------------------
print(f"📁 File dibaca dari path: {file_path}")
