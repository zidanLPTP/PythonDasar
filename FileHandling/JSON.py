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
    print(f"Mengubah {type(data)} ke JSON string...")
    json_str = json.dumps(data, indent=4, separators=(", ", ": "))
    print(json_str)
    return json_str


# ========================
# ✅ dump() → dict → file
# ========================
def buat_JSON_file(data, filename=base_path):
    """Menyimpan dictionary ke file JSON."""
    print(f"Berhasil menyimpan data ke file: {filename}")
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, separators=(", ", ": "))


# ========================
# ✅ load() → file → dict
# ========================
def baca_JSON_file(filename=base_path):
    """Membaca file JSON dan mengembalikan sebagai dict."""
    print(f"Membaca data dari file: {filename}")
    with open(filename, "r") as file:
        data = json.load(file)
    print("Berhasil membaca file JSON jadi dict Python:")
    print(data)
    return data


# ========================
# ✅ loads() → str → dict
# ========================
def string_ke_dict(json_string):
    """Mengubah JSON string ke dictionary."""
    print(f"Mengubah string JSON ke dict...")
    data = json.loads(json_string)
    print("Hasil konversi:")
    print(data)
    return data


# ========================
# Test kalau file dijalankan langsung
# ========================
if __name__ == "__main__":
    print("\n=== dumps() ===\n")
    json_str = JSON_Respon(data_mahasiswa)

    print("\n=== dump() ===\n")
    buat_JSON_file(data_mahasiswa)

    print("\n=== load() ===\n")
    dict_dari_file = baca_JSON_file()

    print("\n=== loads() ===\n")
    dict_dari_string = string_ke_dict(json_str)
