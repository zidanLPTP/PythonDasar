print("maniulasi string di Python")
print("======================================")

# ~ Inisialisasi string
teks = "Belajar Python Seru Banget!"
print("Teks:", teks)
print("Panjang string:", len(teks))

print("\n~ Indexing (mengakses karakter berdasarkan posisi)")
print("Karakter pertama     :", teks[0])    # huruf pertama
print("Karakter kelima      :", teks[4])    # huruf kelima
print("Karakter terakhir    :", teks[-1])   # huruf terakhir
print("Karakter kedua dari akhir:", teks[-2])  # karakter sebelum terakhir

print("\n~ Looping tiap karakter dengan for")
for huruf in teks:
    print(huruf, end=" ")
print()

print("\n======================================")
print("~ SLICING STRING (memotong sebagian teks)")

# Format umum: string[start:stop] atau string[start:stop:step]
print("teks[0:7]      =", teks[0:7])      # dari index 0 sampai 6
print("teks[:7]       =", teks[:7])       # dari awal sampai 6
print("teks[8:]       =", teks[8:])       # dari index 8 sampai akhir
print("teks[0:21:2]   =", teks[0:21:2])   # tiap 2 huruf dari index 0-20

print("\n~ Slicing negatif")
print("teks[-6:-1]    =", teks[-6:-1])    # ambil dari belakang
print("teks[::-1]     =", teks[::-1])     # membalik string

print("\n~ Modifikasi string (tidak bisa langsung diubah)")
# String bersifat immutable, jadi kita harus membuat string baru
nama = "Zidan"
nama_baru = "F" + nama[1:]
print("Nama asli     :", nama)
print("Nama diubah   :", nama_baru)

print("\n~ fungsi pada string")
contoh = "Belajar python itu KEREN dan menyenangkan"

print("Teks awal              :", contoh)
print("~ .upper()             :", contoh.upper())        # Semua huruf kapital
print("~ .lower()             :", contoh.lower())        # Semua huruf kecil
print("~ .capitalize()        :", contoh.capitalize())   # Kapital di awal saja
print("~ .title()             :", contoh.title())        # Setiap kata kapital
print("~ .swapcase()          :", contoh.swapcase())     # Tukar besar-kecil
print("~ .count('a')          :", contoh.count('a'))     # Hitung jumlah huruf 'a'
print("~ .find('python')      :", contoh.find('python')) # Posisi kata 'python'
print("~ .replace('python', 'JavaScript'):", contoh.replace("python", "JavaScript"))
print("~ .startswith('Belajar'):", contoh.startswith("Belajar"))  # Cek awalan
print("~ .endswith('menyenangkan'):", contoh.endswith("menyenangkan"))  # Cek akhiran
print("~ .split()             :", contoh.split())        # Pecah jadi list
print("~ .join('-')           :", '-'.join(['belajar', 'python', 'seru']))  # Gabung list ke string

print("\n~ strip(), lstrip(), rstrip()")
teks_kotor = "   Halo Dunia   "
print("Asli        :", repr(teks_kotor))
print("strip()     :", repr(teks_kotor.strip()))    # Hilang spasi kiri kanan
print("lstrip()    :", repr(teks_kotor.lstrip()))   # Hilang spasi kiri
print("rstrip()    :", repr(teks_kotor.rstrip()))   # Hilang spasi kanan

print("\n~ Ubah huruf jadi code ASCII")
huruf = input("\nMasukkan 1 huruf: ")
if len(huruf) == 1:
    print("Kode ASCII dari", huruf, "adalah", ord(huruf))
else:
    print("Input harus 1 karakter!")
print("\n~ Ubah code ASCII jadi huruf")
angka = int(input("Masukkan kode ASCII (0–1114111): "))
print("Karakter dari kode ASCII", angka, "adalah", chr(angka))

print("\n~ String formating")
depan = input("Nama depan: ")
belakang = input("Nama belakang: ")
kenalan = f"perkenalkan nama saya {depan} {belakang}"