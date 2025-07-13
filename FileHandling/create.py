# ==========================================
# Modul: create.py
# Topik: Membuat dan Menulis File + Penjelasan Mode File
# Cocok untuk: Pemula yang belajar File Handling di Python
# ==========================================

import os

# Dapatkan path folder tempat file .py ini berada
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "contoh_create.txt")

# 1. Membuat dan menulis file teks (mode 'w')
# Mode 'w' akan membuat file baru ATAU menimpa file lama jika sudah ada
with open(file_path, "w") as f:
    f.write("Halo dunia!\n")
    f.write("File ini dibuat dengan mode 'w'\n")

# 2. Menambahkan teks ke file yang sudah ada (mode 'a')
# Mode 'a' akan menambahkan ke akhir file tanpa menghapus isi sebelumnya
with open(file_path, "a") as f:
    f.write("Ini ditambahkan dengan mode 'a'\n")

# 3. Membaca kembali isi file (mode 'r')
# Mode 'r' hanya untuk membaca isi file yang SUDAH ADA
with open(file_path, "r") as f:
    print("\n=== Isi File contoh_create.txt ===")
    print(f.read())

# ==============================
# 📌 Tabel Mode File Python
# ==============================

tabel_mode = """
|-------|------------------------------------------------|
| Mode  | Deskripsi                                      |
|-------|------------------------------------------------|
| 'r'   | Read (baca), file harus sudah ada              |
| 'w'   | Write (tulis), hapus isi lama atau buat baru   |
| 'a'   | Append (tambah di akhir), buat kalau belum ada |
|-------|------------------------------------------------|
"""

print("\n📖 TABEL MODE FILE")
print(tabel_mode)

# Lokasi penyimpanan file
print(f"📁 File disimpan di: {file_path}")
