print("Operator dalam Python")
print("1. Aritmatika")
print("======================================")
# Inisialisasi nilai variabel a dan b
a, b = 30, 3
print("~ Penjumlahan")
print("a + b =", a + b)
print("~ Pengurangan")
print("a - b =", a - b)
print("~ Modulus (sisa bagi)")
print("a % b =", a % b)
print("~ Pembagian (hasil float)")
print("a / b =", a / b)
print("~ Pembagian bulat (floor division)")
print("a // b =", a // b)
print("~ Perkalian")
print("a * b =", a * b)
print("~ Pangkat (eksponen)")
print("a ** b =", a ** b)

print("\n2. Assignment")
print("======================================")
print("~ -= sama dengan a = a - b")
a -= b
print("a -= b, a =", a)
print("--------------------------------------")
print("~ += sama dengan a = a + b")
a += b
print("a += b, a =", a)
print("--------------------------------------")
print("~ *= sama dengan a = a * b")
a *= b
print("a *= b, a =", a)
print("--------------------------------------")
print("~ /= sama dengan a = a / b")
a /= b
print("a /= b, a =", a)

print("\n3. Perbandingan")
print("======================================")
print("Nilai a:", a)
print("Nilai b:", b)
print("~ a == b (sama dengan)")
print("a == b:", a == b)
print("~ a != b (tidak sama dengan)")
print("a != b:", a != b)
print("~ a > b (lebih besar dari)")
print("a > b:", a > b)
print("~ a < b (lebih kecil dari)")
print("a < b:", a < b)
print("~ a <= b (lebih kecil atau sama dengan)")
print("a <= b:", a <= b)
print("~ a >= b (lebih besar atau sama dengan)")
print("a >= b:", a >= b)

print("\n4. Logika (Boolean)")
print("======================================")
a, b = 5, 6
print("Nilai a:", a)
print("Nilai b:", b)
print("~ AND")
print("a > b and a > 5:", a > b and a > 5)
print("~ OR")
print("a < b or a > 3:", a < b or a > 3)
print("~ NOT")
print("not (a < b):", not (a < b))

print("\n5. Membership")
print("======================================")
string1 = "Halo ini adalah perjalanan ku belajar python"
print("Teks:", string1)
print("~ in")
print("'halo' in text:", "halo" in string1)  # False karena huruf kecil
print("'Halo' in text:", "Halo" in string1)  # True
print("~ not in")
print("'a' not in text:", "a" not in string1)
print("'A' not in text:", "A" not in string1)

print("\n6. Identitas (Identity)")
print("======================================")
a, b = 5, 5
print("Nilai a:", a)
print("Nilai b:", b)
print("~ is (identik di memori)")
print("a is b:", a is b)
print("~ is not (tidak identik di memori)")
print("a is not b:", a is not b)

# Contoh lain: tipe data berbeda
string1 = "5"
print("a is string1:", a is string1)  # False
print("a is not string1:", a is not string1)