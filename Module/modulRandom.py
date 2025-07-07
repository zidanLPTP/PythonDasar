import random

print("MODUL: Modul Random di Python")
print("======================================")

# ~ Angka acak dasar
print("\n1. Angka acak")
print("random.random() -> angka acak 0.0 - 1.0 :", random.random())
print("random.uniform(10, 20) -> float 10-20  :", random.uniform(10, 20))
print("random.randint(1, 100) -> int 1-100    :", random.randint(1, 100))
print("random.randrange(1, 100, 5) -> kelipatan 5 dari 1-100:", random.randrange(1, 100, 5))

# ~ Mengambil acak dari list
print("\n2. Pengambilan acak dari list")
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
print("random.choice(buah)     -> satu item :", random.choice(buah))
print("random.choices(buah, k=3) -> 3 item (boleh duplikat):", random.choices(buah, k=3))
print("random.sample(buah, 3)  -> 3 item unik:", random.sample(buah, 3))

# ~ Shuffle (acak urutan)
print("\n3. Mengacak urutan list")
angka = list(range(10))
print("Sebelum diacak:", angka)
random.shuffle(angka)
print("Setelah diacak:", angka)

# ~ Simulasi lempar dadu
print("\n4. Simulasi Lempar Dadu (1–6)")
for i in range(5):
    print("Lemparan ke-", i+1, ":", random.randint(1, 6))

# ~ Random dengan seed
print("\n5. Seed (reproducible randomness)")
random.seed(42)
print("Angka acak setelah seed(42):", random.randint(1, 100))
random.seed(42)
print("Angka acak lagi setelah seed(42):", random.randint(1, 100))

# ~ Mini Project: Tebak Angka
print("\n6. Mini Project: Game Tebak Angka (1-10)")
jawaban = random.randint(1, 10)
percobaan = 5
while percobaan > 0:
    coba = int(input("Tebak angka dari 1 sampai 10: "))
    percobaan -= 1
    if coba == jawaban:
        print("Tepat! Kamu hebat.")
        break
    else:
        print("salah, ayo coba lagi")
        print("percobaan kamu:",percobaan)

        if percobaan == 0:
            print("kamu gagal, jawabannya;", jawaban)


# ~ Ringkasan Fungsi Random
print("\n7. Ringkasan Fungsi random")
fungsi_random = [
    "random.random()         -> float dari 0.0 sampai <1.0",
    "random.uniform(a, b)    -> float dari a sampai b",
    "random.randint(a, b)    -> integer dari a sampai b",
    "random.randrange(start, stop, step) -> seperti range(), acak",
    "random.choice(seq)      -> satu elemen acak dari list/tuple/str",
    "random.choices(seq, k=n)-> n elemen, boleh duplikat",
    "random.sample(seq, n)   -> n elemen unik",
    "random.shuffle(list)    -> acak urutan list (in-place)",
    "random.seed(x)          -> untuk reproducible randomness"
]

for f in fungsi_random:
    print("-", f)
