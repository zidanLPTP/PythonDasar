print("Lambda Function dalam Python")
print("======================================")

print("\n~ Apa itu Lambda?")
penjelasan = (
    "Lambda adalah fungsi anonim di Python, artinya fungsi yang tidak diberi nama eksplisit.\n"
    "Biasanya digunakan untuk fungsi sederhana dalam satu baris."
)
print(penjelasan)

# Contoh dasar lambda
print("\n~ Contoh Dasar")
tambah = lambda x, y: x + y
print("Lambda untuk penjumlahan: lambda x, y: x + y")
print("Hasil dari tambah(4, 5):", tambah(4, 5))

kuadrat = lambda x: x ** 2
print("Lambda untuk kuadrat: lambda x: x ** 2")
print("Hasil dari kuadrat(6):", kuadrat(6))

print("\n~ Lambda dengan fungsi map()")
angka = [1, 2, 3, 4, 5]
print("List awal:", angka)
hasil_map = list(map(lambda x: x * 2, angka))
print("Hasil map (x*2):", hasil_map)

print("\n~ Lambda dengan fungsi filter()")
ganjil = list(filter(lambda x: x % 2 != 0, angka))
print("Filter angka ganjil:", ganjil)

print("\n~ Lambda dengan fungsi sorted()")
siswa = [("Zidan", 90), ("Manda", 98), ("Daffa", 88), ("Nabila", 95)]
print("Data siswa:", siswa)
urut_nilai = sorted(siswa, key=lambda x: x[1], reverse=True)
print("Urut berdasarkan nilai tertinggi:", urut_nilai)

print("\n~ Lambda dalam list comprehension")
hitung = [(lambda x: x + 3)(i) for i in range(5)]
print("Tambah 3 untuk setiap elemen:", hitung)

print("\n~ Lambda Bersarang (Nested)")
operasi = lambda x: (lambda y: x + y)
print("Fungsi lambda bersarang untuk penjumlahan:")
print("operasi(10)(5):", operasi(10)(5))

print("\n~ Lambda dengan kondisi (if-else)")
cek_genap = lambda x: "Genap" if x % 2 == 0 else "Ganjil"
print("Angka 4 adalah:", cek_genap(4))
print("Angka 7 adalah:", cek_genap(7))

print("\n~ Lambda di dalam fungsi biasa")
def pembuat_pangkat(n):
    return lambda x: x ** n

pangkat3 = pembuat_pangkat(3)
print("Hasil dari pangkat3(2):", pangkat3(2))  # 2 ** 3 = 8

print("\n~ Perbandingan Fungsi Biasa vs Lambda")
def fungsi_biasa(x): return x + 1
fungsi_lambda = lambda x: x + 1

print("fungsi_biasa(5):", fungsi_biasa(5))
print("fungsi_lambda(5):", fungsi_lambda(5))

print("\n~ Kasus Praktis: Sortir berdasarkan panjang string")
kata = ["pisang", "apel", "pepaya", "jeruk"]
urut_kata = sorted(kata, key=lambda x: len(x))
print("Sebelum disortir:", kata)
print("Setelah disortir berdasarkan panjang:", urut_kata)

print("\n~ Kesimpulan")
print("- Lambda digunakan untuk fungsi singkat dan instan")
print("- Tidak cocok untuk fungsi kompleks atau multiline")
print("- Sering dipakai di map(), filter(), sorted(), dll")

print("\nSilakan eksplorasi lambda function dalam konteks kamu sendiri. Gunakan lambda bila fungsinya cukup ringkas dan hanya dipakai sekali dua kali.")
