# ===================================================
# Modul: write.py
# Topik: Menulis & Membaca File (Mode: 'a+')
# Cocok untuk: Pemula belajar file handling di Python
# ===================================================

import os

# ================================================
# 📌 1. Menentukan path file secara dinamis
# Tujuan: supaya file tetap bisa digunakan walau foldernya dipindah
# __file__ → nama file Python ini
# ================================================
BASE_DIR = os.path.dirname(__file__)  # Direktori file ini
file_path = os.path.join(BASE_DIR, "contoh_create.txt")  # Path lengkap ke file

# ================================================
# 📌 2. Menulis dan membaca file dengan mode 'a+'
# Mode 'a+' = append + read (tulis di akhir & bisa baca)
# Jika file tidak ada, Python akan otomatis membuatnya
# ================================================
with open(file_path, "a+") as file:
    # ✍️ Tambahkan teks baru di akhir file
    file.write("\n📌 Teks ini ditambahkan dari write_file_append_read.py")

    # 📖 Pindahkan kursor ke awal supaya bisa membaca dari awal
    file.seek(0)

    # 🖨️ Tampilkan isi file
    print(f"\n=== Isi dari file: {file_path} ===")
    print(file.read())

# ================================================
# 📖 TABEL MODE FILE (KHUSUS UNTUK WRITE)
# ================================================

tabel_mode_write = """
| Mode  | Deskripsi                                                                 |
|-------|---------------------------------------------------------------------------|
| 'w'   | Write: menulis ke file, jika file ada akan ditimpa                        |
| 'a'   | Append: menulis di akhir file, jika file tidak ada maka dibuat           |
| 'x'   | Create-only: membuat file baru, error jika file sudah ada                |
| 'w+'  | Write + Read: menulis & membaca, file ditimpa jika sudah ada             |
| 'a+'  | Append + Read: menulis di akhir & bisa membaca, file dibuat jika belum ada |
| 'x+'  | Create + Read: buat file baru + baca, error jika file sudah ada          |
"""

print("\n📄 TABEL MODE WRITE FILE:")
print(tabel_mode_write)

# ================================================
# KESIMPULAN:
# Gunakan mode sesuai kebutuhan:
# - 'w' untuk mengganti isi
# - 'a' untuk menambahkan
# - 'x' untuk membuat baru (dan error kalau sudah ada)
# - gunakan mode + untuk bisa membaca juga
# ================================================
