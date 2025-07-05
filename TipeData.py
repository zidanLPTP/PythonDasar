print("Tipe data dalam Python\n")

# 1. Sequence Type
print("1. Sequence Type")
print("======================================")
print("~ String")
namaDepan = "Fathin "
namaTengah = 'Ahmad '
namaBelakang = "Zidan"
nama = namaDepan + namaTengah + namaBelakang
hobi = '''
    Saya tertarik untuk mempelajari berbagai bahasa pemrograman.
    Sejauh ini saya sudah belajar C++, JavaScript, Kotlin dan 
    kali ini aku akan belajar Python.
'''
print("Nama lengkapku adalah", nama)
print("Hobiku:", hobi)

print("--------------------------------------")
print("~ List (nilai bisa dirubah)")
mobil = ["BMW", "HONDA", "TOYOTA", "VOLVO"]
print("Isi pertama dari list mobil:", mobil[0])

print("--------------------------------------")
print("~ Tuple (nilai tidak bisa diubah)")
nilai = (98, 90, 95, 80)
print("Isi pertama dari tuple nilai:", nilai[0])

# 2. Number
print("\n2. Number")
print("======================================")
angka1 = 10
angka2 = 20
angka3 = 3.14
angka4 = 0.5
a = 10 + 5j

print("--------------------------------------")
print("~ Integer")
print("nilai:", angka1)
print("Penjumlahan:", angka1 + angka2)

print("--------------------------------------")
print("~ Float")
print("nilai:", angka3)
print("Penjumlahan:", angka3 + angka4)

print("--------------------------------------")
print("~ Complex")
print("nilai:", a)

# 3. Dictionary
print("\n3. Dictionary")
print("======================================")
Data = {
    "nama": "Fathin Ahmad Zidan A",
    "NIM": 2407112398,
    "umur": 20,
    "negara": "ID"
}
print("Key 'nama' menyimpan:", Data['nama'])
print("Key 'umur' menyimpan:", Data['umur'])

# 4. Set
print("\n4. Set")
print("======================================")
print("Kumpulan item unik (tidak bisa duplikat)")
data_set = {1, 2, 3, 4, 5, 1, 2}
print("Isi set:", data_set)

# 5. Boolean dan None

print("\n5. Boolean dan None")
print("======================================")
aktif = True
kosong = None
print("Status aktif:", aktif)
print("Kosong:", kosong)

# ID dan TYPE
print("\n======================================")
print("Menampilkan alamat variabel dengan id()")
print("Alamat angka3:", id(angka3))
print("Alamat namaDepan:", id(namaDepan))

print("\nMenampilkan tipe data variabel dengan type()")
print("Tipe nama:", type(nama))
print("Tipe mobil:", type(mobil))
print("Tipe nilai:", type(nilai))
print("Tipe angka1:", type(angka1))
print("Tipe angka4:", type(angka4))
print("Tipe a:", type(a))
print("Tipe Data (dict):", type(Data))
print("Tipe data_set:", type(data_set))
print("Tipe aktif:", type(aktif))
print("Tipe kosong:", type(kosong))