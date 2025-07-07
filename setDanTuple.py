print("Tuple di Python (Immutable List)")
print("======================================")

# ~ Inisialisasi Tuple
nilai = (90, 85, 88, 95)
print("Isi Tuple:", nilai)
print("Tipe data:", type(nilai))
print("Panjang tuple:", len(nilai))

# ~ Akses indeks
print("\n~ Akses elemen")
print("Elemen pertama:", nilai[0])
print("Elemen terakhir:", nilai[-1])
print("Slicing elemen ke-2 sampai 4:", nilai[1:4])

# ~ Perulangan pada Tuple
print("\n~ Looping isi tuple")
for i in nilai:
    print("Nilai:", i)

# ~ Nested Tuple
print("\n~ Tuple bersarang")
nested = (1, 2, ("Python", "JavaScript"), 3)
print("Tuple nested:", nested)
print("Akses elemen 'JavaScript':", nested[2][1])

# ~ Tuple hanya bisa dibaca, tidak bisa diubah langsung
print("\n~ Tuple bersifat immutable (tidak bisa diubah)")
try:
    nilai[0] = 100  # ini akan error
except TypeError as e:
    print("Error:", e)

# ~ Konversi dari list ke tuple
print("\n~ Konversi list ke tuple")
daftar = [1, 2, 3]
tpl = tuple(daftar)
print("Tuple dari list:", tpl)

print("\nSet di Python (Unordered, Unique Values)")
print("======================================")

# ~ Inisialisasi Set
buah = {"apel", "jeruk", "mangga", "jeruk", "apel"}
print("Isi Set (tidak ada duplikat):", buah)
print("Tipe data:", type(buah))

# ~ Looping set
print("\n~ Looping isi set")
for item in buah:
    print("Buah:", item)

# ~ Menambah elemen
print("\n~ Menambahkan elemen")
buah.add("pisang")
print("Set setelah add:", buah)

# ~ Menambah banyak elemen
buah.update(["anggur", "durian"])
print("Set setelah update:", buah)

# ~ Menghapus elemen
buah.discard("jeruk")  # tidak error jika elemen tidak ada
print("Set setelah discard 'jeruk':", buah)

buah.remove("apel")  # error jika tidak ada
print("Set setelah remove 'apel':", buah)

# ~ Pop (acak)
terambil = buah.pop()
print("Hapus acak (pop):", terambil)
print("Set sekarang:", buah)

# ~ Clear semua elemen
buah.clear()
print("Set setelah clear:", buah)

# ~ Operasi Set
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print("\n~ Operasi himpunan")
print("A:", setA)
print("B:", setB)
print("Gabungan (union):", setA.union(setB))
print("Irisan (intersection):", setA.intersection(setB))
print("Selisih A - B:", setA.difference(setB))
print("Selisih B - A:", setB.difference(setA))
print("Gabungan menggunakan '|':", setA | setB)
print("Irisan menggunakan '&':", setA & setB)
print("Selisih menggunakan '-':", setA - setB)
print("Apakah A subset dari B?", setA.issubset(setB))
print("Apakah A dan B disjoint?", setA.isdisjoint(setB))
