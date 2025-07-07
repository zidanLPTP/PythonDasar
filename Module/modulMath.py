# Modul Belajar: Modul math di Python
import math

print("MODUL: Fungsi Matematika (math)")
print("==========================================")

#digunakan di math.fsum()
data = [23,43,54,223,12,43]

# ~ Aritmatika Dasar
print("\n1. Aritmatika Dasar")
print("Akar kuadrat dari 25      :", math.sqrt(25))
print("Pangkat 2^3               :", math.pow(2, 3))
print("Pembulatan ke atas (4.2)  :", math.ceil(4.2))
print("Pembulatan ke bawah (4.9) :", math.floor(4.9))
print("Nilai mutlak dari -7      :", math.fabs(-7))
print("Menambahkan semua data    :", math.fsum(data))

# ~ Trigonometri
print("\n2. Fungsi Trigonometri (pakai radian)")
print("Sinus 90°     :", math.sin(math.radians(90)))
print("Cosinus 0°    :", math.cos(math.radians(0)))
print("Tangen 45°    :", math.tan(math.radians(45)))

# ~ Logaritma & Konstanta
print("\n3. Logaritma dan Konstanta")
print("Log e         :", math.log(math.e))
print("Log10 dari 1000:", math.log10(1000))
print("π (pi)        :", math.pi)
print("e (Euler)     :", math.e)

# ~ Fungsi Khusus
print("\n4. Fungsi Matematika Lainnya")
print("Faktorial 5   :", math.factorial(5))
print("GCD dari 24 dan 36 :", math.gcd(24, 36))
try:
    print("LCM dari 4 dan 6   :", math.lcm(4, 6))  # Python 3.9+
except AttributeError:
    print("LCM tidak tersedia (butuh Python 3.9+)")

# ~ Mini Project: Hitung Luas dan Keliling Lingkaran
print("\n5. Hitung Luas dan Keliling Lingkaran")
try:
    r = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * math.pow(r, 2)
    keliling = 2 * math.pi * r
    print("Luas      =", luas)
    print("Keliling  =", keliling)
except:
    print("Input tidak valid.")

# ~ Ringkasan Fungsi Umum
print("\n6. Ringkasan Fungsi math")
fungsi_math = [
    "math.sqrt(x)       -> Akar kuadrat",
    "math.pow(x, y)     -> Pangkat",
    "math.ceil(x)       -> Pembulatan ke atas",
    "math.floor(x)      -> Pembulatan ke bawah",
    "math.fabs(x)       -> Nilai mutlak",
    "math.factorial(x)  -> Faktorial",
    "math.log(x)        -> Logaritma natural",
    "math.log10(x)      -> Log basis 10",
    "math.sin(x)        -> Sinus (radian)",
    "math.cos(x)        -> Cosinus (radian)",
    "math.tan(x)        -> Tangen (radian)",
    "math.gcd(x, y)     -> FPB",
    "math.lcm(x, y)     -> KPK (Python 3.9+)",
]

for f in fungsi_math:
    print("-", f)
