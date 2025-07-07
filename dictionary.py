print("Dictionary di Python")
print("======================================")

# ~ Inisialisasi dictionary
data = {
    "nama": "Fathin Ahmad Zidan",
    "umur": 20,
    "pekerjaan": "Kuliah",
    "aktif": True
}

# ~ Akses isi dictionary
print("\n~ Cara mengakses isi dictionary")
for key in data:
    print(key, ":", data[key])

# ~ Fungsi-fungsi umum
print("\n~ Beberapa fungsi/metode khusus dictionary")
print("~ .keys()")
print("Menampilkan semua key:")
for key in data.keys():
    print(key)

print("~ .values()")
print("Menampilkan semua value:")
for value in data.values():
    print(value)

print("~ .items()")
print("Menampilkan pasangan key dan value:")
for key, value in data.items():
    print(key, ":", value)

# ~ Menambahkan elemen
print("\n~ Menambahkan data baru")
data["hobi"] = "Programming"
print("Setelah menambah key 'hobi':", data)

# ~ Mengupdate isi dictionary
print("\n~ Mengupdate data")
data["umur"] = 21
print("Setelah update umur:", data)

# ~ Menghapus data dengan del
print("\n~ Menghapus key dengan 'del'")
del data["aktif"]
print("Setelah del 'aktif':", data)

# ~ Menghapus dan mengembalikan item dengan pop()
print("\n~ Menghapus dan mengembalikan nilai dengan pop()")
pekerjaan = data.pop("pekerjaan")
print("Data pekerjaan yang dihapus:", pekerjaan)
print("Data sekarang:", data)

# ~ Mengecek apakah key ada
print("\n~ Mengecek keberadaan key")
print("Apakah 'nama' ada di data?", "nama" in data)
print("Apakah 'alamat' ada di data?", "alamat" in data)

# ~ Menggabungkan dua dictionary
print("\n~ Menggabungkan dua dictionary dengan update()")
data_tambahan = {"alamat": "Pekanbaru", "umur": 22}
data.update(data_tambahan)
print("Setelah update:", data)

# ~ Menghapus semua isi dictionary
print("\n~ Menghapus semua isi dictionary dengan clear()")
data.clear()
print("Setelah clear():", data)
