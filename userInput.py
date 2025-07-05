print("User Input dalam Python")
print("======================================")

# ~ Penjelasan dasar input
print("~ Mengisi Data Diri (String Input)")
nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")          # Masih berupa string
pekerjaan = input("Masukkan pekerjaan: ")

print("\n~ Menampilkan Kembali Data Diri")
print("Nama       :", nama)
print("Umur       :", umur)
print("Pekerjaan  :", pekerjaan)
print("======================================")

# ~ Konversi input ke tipe data yang sesuai
print("\n~ Operasi Aritmatika")
angka1 = input("Masukkan angka pertama: ")
angka2 = input("Masukkan angka kedua: ")

# ⚠️ eval() bisa digunakan, tapi ada risiko keamanan jika input dari user tidak terpercaya
# Disarankan konversi eksplisit
try:
    a = float(angka1)
    b = float(angka2)
    print("Hasil penjumlahan adalah:", a + b)
    print("Hasil pengurangan adalah:", a - b)
    print("Hasil perkalian adalah:", a * b)
    print("Hasil pembagian adalah:", a / b)
except ValueError:
    print("Input harus berupa angka!")

print("======================================")

# ~ Boolean input (konversi manual)
print("\n~ Boolean Input")
belajar = input("Apakah kamu suka belajar Python? (yes/no): ")
is_suka_python = belajar.lower() == "yes"
print("Suka Python:", is_suka_python)
print("Tipe data:", type(is_suka_python))

print("======================================")

# ~ Menampilkan tipe data dari semua input
print("~ Cek Tipe Data dari Input")
print("Tipe data nama       :", type(nama))
print("Tipe data umur       :", type(umur))        # masih string
print("Tipe data pekerjaan  :", type(pekerjaan))
print("Tipe data angka1     :", type(angka1))      # masih string
print("Tipe data setelah konversi (a) :", type(a)) # float