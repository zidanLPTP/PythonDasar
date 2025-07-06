print("List dalam Python")
print("======================================")

# ~ Bisa berisi berbagai tipe data
definisi = "List adalah kumpulan elemen yang dapat menyimpan berbagai tipe data."
print("\n~ Mengerti list")
isiList = [1, 2, 4, False, True,["aku", "juga", "disini"], 3.14, "Python", [1, 2, 3, True, False, "ayam"]]
total = len(isiList)  # jumlah elemen dalam list
print("Contoh list:", isiList)
print("Panjang list:", total)
print("\nSampai elemen ke-7:", isiList[:7])  # slicing sampai indeks ke-6
print("Akses elemen list di dalam list:", isiList[-1][2])  # akses elemen ke-3 dari nested list
print("Elemen pertama:", isiList[0])
print("Elemen terakhir:", isiList[-1])
print("Tiga elemen pertama:", isiList[:3])
print("Tiap dua elemen:", isiList[::2])

print("\n~ Perulangan Python di list")
# Gunakan enumerate() untuk mendapatkan indeks dan nilai secara bersamaan
for i, var in enumerate(isiList):
    print(f"isi ke-{i} berisi {var}")
    # isinstance(var, list) mengecek apakah elemen saat ini bertipe list
    if isinstance(var, list):
        print(f"\nIsi dari isi ke-{i} adalah")
        for ii, subvar in enumerate(var):
            print(f"indeks-{ii} dari {subvar}")
        print()

print("\n~ List Comprehension")
# Membuat list baru dari range menggunakan kondisi dan ekspresi ringkas
angka = [i for i in range(1, 21)]
print("Isi list angka:", angka)
angka_ganjil = [i for i in range(1, 21) if i % 2 != 0]
print("Isi list angka ganjil:", angka_ganjil)
angka_genap = [i for i in range(1, 21) if i % 2 == 0]
print("Isi list angka genap:", angka_genap)

print("\n~ Penghapusan Elemen dalam List di Python")
print("===========================================")

buah = ['apel', 'jeruk', 'mangga', 'pisang', 'jeruk']
print("List awal:", buah)

# ~ 1. del: Hapus elemen berdasarkan INDEKS
print("\n1. Menggunakan 'del'")
print("Hapus elemen di indeks ke-1 (jeruk)")
del buah[1]  # menghapus elemen indeks 1
print("List setelah 'del buah[1]':", buah)

# ~ 2. pop(): Hapus dan KEMBALIKAN NILAI berdasarkan INDEKS
print("\n2. Menggunakan 'pop()'")
print("Hapus dan ambil elemen terakhir")
terambil = buah.pop()  # default: menghapus elemen terakhir
print("Elemen yang di-pop:", terambil)
print("List setelah 'pop()':", buah)

print("Hapus dan ambil elemen indeks ke-1")
terambil2 = buah.pop(1)  # menghapus elemen indeks ke-1
print("Elemen yang di-pop:", terambil2)
print("List setelah 'pop(1)':", buah)

# ~ 3. remove(): Hapus berdasarkan NILAI
print("\n3. Menggunakan 'remove()'")
buah.append('jeruk')  # tambahkan jeruk agar bisa dihapus
print("Sebelum remove:", buah)
buah.remove('jeruk')  # hanya menghapus jeruk pertama yang ditemukan
print("List setelah 'remove(\"jeruk\")':", buah)

# ~ 4. clear(): Menghapus semua elemen dalam list
print("\n4. Menggunakan 'clear()'")
print("List sebelum clear():", buah)
buah.clear()  # menghapus semua elemen
print("List setelah 'clear()':", buah)

print("\nFungsi Built-in Umum pada List")
print("===========================================")

angka = [45, 12, 89, 33, 67, 12, 90]
print("List angka:", angka)

# ~ min() dan max(): Mengembalikan nilai terkecil dan terbesar
print("\n~ min() dan max()")
print("Nilai terkecil (min):", min(angka))
print("Nilai terbesar (max):", max(angka))

# ~ sum(): Menjumlahkan semua elemen
print("\n~ sum()")
print("Jumlah semua elemen:", sum(angka))

# ~ sorted(): Mengembalikan list baru yang sudah diurutkan
print("\n~ sorted()")
print("List ascending:", sorted(angka))
print("List descending:", sorted(angka, reverse=True))
print("List asli tetap:", angka)  # tidak berubah

# ~ sort(): Mengurutkan list secara langsung (in-place)
print("\n~ sort()")
angka.sort()
print("List setelah sort():", angka)
angka.sort(reverse=True)
print("List setelah sort(reverse=True):", angka)

# ~ reverse(): Membalik urutan list
print("\n~ reverse()")
angka.reverse()
print("List setelah reverse():", angka)

# ~ count(): Menghitung kemunculan elemen tertentu
print("\n~ count()")
print("Jumlah angka '12' muncul:", angka.count(12))

# ~ index(): Mendapatkan indeks dari elemen pertama yang cocok
print("\n~ index()")
print("Indeks pertama dari angka 90:", angka.index(90))

# ~ copy(): Menyalin list
print("\n~ copy()")
salinan = angka.copy()
print("Salinan list:", salinan)

# ~ extend(): Menambahkan banyak elemen ke list
print("\n~ extend()")
angka.extend([100, 200])
print("Setelah extend:", angka)

# ~ insert(): Menyisipkan elemen pada posisi tertentu
print("\n~ insert()")
angka.insert(2, 999)  # masukkan 999 di indeks ke-2
print("Setelah insert:", angka)

# ~ zip(): Menggabungkan dua list menjadi pasangan tuple
print("\n~ fungsi zip() di list")
nama = ["Zidan", "Manda", "Dayana", "Daffa", "Nabila"]
nilai = [98, 97, 99, 96, 90]
print("Nama:", nama)
print("Nilai:", nilai)
hasil = zip(nama, nilai)  # zip menggabungkan list
print("Tipe hasil sebelum diubah:", type(hasil))
print("Hasil zip dalam bentuk list:", list(hasil))

# ~ split(): Membuat string menjadi list
print("\n~ split()")
inputKu = input("Masukkan string anda: ")
jadiList = inputKu.split()
print(jadiList)

