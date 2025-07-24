import json
import os

# Path default file JSON
path = os.path.dirname(__file__)
base_path = os.path.join(path, "Data.json")

# Data untuk testing awal
data_mahasiswa = {
    "nama": "Zidan",
    "umur": 20,
    "ipk": 3.75,
    "aktif": True,
    "alamat": {
        "kota": "Pekanbaru",
        "provinsi": "Riau",
        "kode_pos": 28293
    },
    "hobi": ["ngoding", "baca buku", "ngopi"],
    "jadwal_kuliah": (
        ("Senin", "Matematika Diskrit"),
        ("Selasa", "Struktur Data"),
        ("Rabu", "Web Programming")
    ),
    "nilai_ujian": {
        "uts": 88,
        "uas": 91,
        "kuis": [80, 85, 90]
    },
    "magang": None,
    "is_admin": False
}

# ========================
# ✅ dumps() → dict → str
# ========================
def JSON_Respon(data):
    """Mengubah dictionary ke JSON string dan print hasilnya."""
    print("\n🟦 FUNGSI: JSON_Respon(data)")
    print("Mengubah dictionary Python jadi JSON string pakai json.dumps()")
    print(f"Tipe awal: {type(data)}")
    json_str = json.dumps(data, indent=4, separators=(", ", ": "))
    print("✅ Hasil JSON String:\n")
    print(json_str)
    return json_str

# ========================
# ✅ dump() → dict → file
# ========================
def buat_JSON_file(data, filename=base_path):
    """Menyimpan dictionary ke file JSON."""
    print("\n💾 FUNGSI: buat_JSON_file(data)")
    print(f"Menyimpan data ke file JSON di: {filename}")
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, separators=(", ", ": "))
    print("✅ Data berhasil disimpan ke file.")

# ========================
# ✅ load() → file → dict
# ========================
def baca_JSON_file(filename=base_path):
    """Membaca file JSON dan mengembalikan sebagai dict."""
    print("\n📂 FUNGSI: baca_JSON_file()")
    print(f"Membaca file JSON dari: {filename}")
    with open(filename, "r") as file:
        data = json.load(file)
    print("✅ File berhasil dibaca dan dikonversi ke dict:")
    print(data)
    return data

# ========================
# ✅ loads() → str → dict
# ========================
def string_ke_dict(json_string):
    """Mengubah JSON string ke dictionary."""
    print("\n🔄 FUNGSI: string_ke_dict(json_string)")
    print("Mengonversi string JSON ke dictionary Python pakai json.loads()")
    data = json.loads(json_string)
    print("✅ Hasil konversi string ke dict:")
    print(data)
    return data

# ========================
# ✅ Jika dijalankan langsung
# ========================
if __name__ == "__main__":
    print("📦 MODUL PENGOLAHAN JSON PYTHON")
    print("===============================")

    print("\n=== [1] dumps() ===")
    json_str = JSON_Respon(data_mahasiswa)

    print("\n=== [2] dump() ===")
    buat_JSON_file(data_mahasiswa)

    print("\n=== [3] load() ===")
    dict_dari_file = baca_JSON_file()

    print("\n=== [4] loads() ===")
    dict_dari_string = string_ke_dict(json_str)

    print("\n✅ Selesai semua operasi JSON.\n")