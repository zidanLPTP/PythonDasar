import json

print("Serialisasi & Deserialisasi dengan JSON di Python")
print("===============================================")

# # ==============================================
# # CARA 1: Simpan dan baca objek ke/dari file
# # ==============================================
# print("\n~ Cara 1: Simpan objek Python ke dalam file JSON")

# # Data yang akan disimpan
# data1 = {
#     "nama": "Fathin Ahmad Zidan",
#     "umur": 20,
#     "tinggi": 170,
#     "kuliah": True,
#     "jurusan": "Teknik Informatika",
#     "gaji": "Rp. 300.000"
# }

# # Simpan data ke file JSON menggunakan mode "w"
# with open("dataJSON.json", "w") as file_json:
#     json.dump(data1, file_json, indent=4)  # indent agar rapi
#     print("Data berhasil disimpan ke 'dataJSON.json'")

# # Baca kembali data dari file menggunakan mode "r"
# with open("dataJSON.json", "r") as file_json:
#     loaded_data = json.load(file_json)
#     print("\nData yang dibaca dari file:")
#     for key, value in loaded_data.items():
#         print(f"{key} : {value}")

# ==============================================
# CARA 2: Serialisasi ke dalam string JSON (bukan file)
# ==============================================
print("\n~ Cara 2: Simpan objek Python ke dalam string JSON (di memori)")

data2 = {
    "nama": "Fathin Zidan",
    "umur": 21,
    "tinggi": 170,
    "kuliah": True,
    "jurusan": "Sistem Informasi",
    "gaji": "Rp. 200.000"
}

# Serialize ke string JSON
json_string = json.dumps(data2, indent=4)
print("\nData yang dikonversi ke string JSON:")
print(json_string)

# Deserialize kembali dari string JSON
recovered_data = json.loads(json_string)
print("\nData yang di-recover dari string JSON:")
for key, value in recovered_data.items():
    print(f"{key} : {value}")

print("\nSelesai. JSON cocok untuk interoperabilitas (misalnya kirim antar sistem).")
