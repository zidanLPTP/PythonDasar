import pickle

print("Serialisasi & Deserialisasi dengan Pickle di Python")
print("===============================================")

# ==============================================
# CARA 1: Simpan dan baca objek ke/dari file
# ==============================================
print("\n~ Cara 1: Simpan objek Python ke dalam file menggunakan pickle")

# Data yang akan disimpan
data1 = {
    "nama": "Fathin Ahmad Zidan",
    "umur": 20,
    "tinggi": 170,
    "kuliah": True,
    "jurusan": "Teknik Informatika",
    "gaji": "Rp. 300.000"
}

# Simpan data ke file menggunakan mode wb (write binary)
with open("dataPickle.txt", "wb") as file_pickle:
    pickle.dump(data1, file_pickle)
    print("Data berhasil disimpan ke 'dataPickle.txt'")

# Baca kembali data dari file menggunakan mode rb (read binary)
with open("dataPickle.txt", "rb") as file_pickle:
    loaded_data = pickle.load(file_pickle)
    print("\nData yang dibaca dari file:")
    for key, value in loaded_data.items():
        print(f"{key} : {value}")

# ==============================================
# CARA 2: Serialisasi ke dalam byte (bukan file)
# ==============================================
print("\n~ Cara 2: Simpan objek Python ke dalam byte")

# Data lain yang akan di-serialize langsung ke memory
data2 = {
    "nama": "Fathin  Zidan",
    "umur": 21,
    "tinggi": 170,
    "kuliah": True,
    "jurusan": "Sistem informasi",
    "gaji": "Rp. 200.000"
}

# Serialize ke byte object
byte_data = pickle.dumps(data2)

# Deserialize kembali dari byte
recovered_data = pickle.loads(byte_data)

print("\nData yang di-recover dari byte:")
for key, value in recovered_data.items():
    print(f"{key} : {value}")

print("\nSelesai. Kedua metode di atas bisa digunakan sesuai kebutuhan.")
