print("Perulangan (Loops) dalam Python")
print("======================================")

# ~ FOR Loop dasar
print("\n~ FOR Loop dengan list")
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print("Saya suka", item)

print("--------------------------------------")

# ~ range() satu parameter
print("\n~ range(5): dari 0 sampai 4")
for i in range(5):
    print("Angka:", i)

# ~ range() dua parameter
print("\n~ range(1, 6): dari 1 sampai 5")
for i in range(1, 6):
    print("Angka:", i)

# ~ range() tiga parameter (dengan step)
print("\n~ range(1, 10, 2): dari 1 ke 9 loncat 2")
for i in range(1, 10, 2):
    print("Angka:", i)

print("======================================")

# ~ WHILE loop dasar
print("\n~ WHILE Loop")
angka = 1
while angka <= 5:
    print("Angka ke:", angka)
    angka += 1

print("======================================")

# ~ CONTINUE dalam loop
print("\n~ CONTINUE: Lewati angka 3")
for i in range(1, 6):
    if i == 3:
        continue
    print("Angka:", i)

print("======================================")

# ~ BREAK dalam loop
print("\n~ BREAK: Hentikan saat angka 4")
for i in range(1, 6):
    if i == 4:
        print("Break di angka", i)
        break
    print("Angka:", i)

print("======================================")

# ~ PASS dalam loop
print("\n~ PASS: Tidak melakukan apa-apa saat angka 2")
for i in range(1, 4):
    if i == 2:
        pass  # bisa dipakai untuk placeholder
    print("Angka:", i)

print("======================================")

# ~ Studi Kasus: Input dan skip ganjil
print("\n~ Studi Kasus: Tampilkan bilangan genap hingga n")
n = int(input("Masukkan angka maksimal: "))
print("Bilangan genap dari 1 sampai", n, ":")
for i in range(1, n + 1):
    if i % 2 != 0:
        continue
    print(i)

print("======================================")
print("Program selesai.")
