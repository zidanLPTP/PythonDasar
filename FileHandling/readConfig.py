# ================================================
# Modul: modul_config_reader.py
# Topik: Membaca file konfigurasi .ini secara umum
# Cocok untuk: Developer yang ingin akses config fleksibel
# ================================================

import os
import configparser

# 📌 1. Tentukan path ke file konfigurasi (config.ini)
# __file__: lokasi file .py ini berada
path = os.path.dirname(__file__)  # direktori file skrip
base_path = os.path.join(path, "config.ini")  # gabung dengan nama file

# 📖 2. Inisialisasi parser untuk membaca file .ini
parser = configparser.ConfigParser()
parser.read(base_path)

# 🧾 3. Loop semua section dan item
print("\n📖 Membaca isi file config.ini")
print("=" * 40)

for section in parser.sections():
    print(f"\n🔹 Section: [{section}]")
    print("  🔑 Keys:", parser.options(section))
    for key, value in parser.items(section):
        print(f"   - {key} : {value}")