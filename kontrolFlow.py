print("Kontrol Flow Dasar dalam Python")
print("======================================")

# ~ Input dan percabangan sederhana
nama = input("Masukkan nama kamu: ")
umur = int(input("Masukkan umur kamu: "))

print("\n~ Percabangan umur")
if umur >= 18:
    print(f"Halo {nama}, kamu sudah dewasa.")
else:
    print(f"Halo {nama}, kamu masih di bawah umur.")

print("======================================")

# ~ Boolean input dengan kontrol flow
print("\n~ Boolean Input dengan If")
belajar = input("Apakah kamu suka belajar Python? (yes/no): ")
is_suka_python = belajar.lower() == "yes"

if is_suka_python:
    print("Mantap! Semangat terus belajar Python 💪🔥")
else:
    print("Gak apa-apa, mungkin kamu belum kenal Python lebih jauh 🙂")

print("Tipe data dari 'is_suka_python':", type(is_suka_python))
print("======================================")

# ~ Contoh if - elif - else
print("\n~ Penilaian Ujian")
nilai = float(input("Masukkan nilai ujian kamu: "))

if nilai >= 90:
    print("Predikat: A (Sangat Baik)")
elif nilai >= 80:
    print("Predikat: B (Baik)")
elif nilai >= 70:
    print("Predikat: C (Cukup)")
else:
    print("Predikat: D (Perlu belajar lebih giat)")

print("======================================")

# ~ Studi kasus kecil: jurusan
print("\n~ Studi Kasus: Jurusan Kuliah")
jurusan = input("Masukkan jurusan kamu: ").lower()

if jurusan == "informatika":
    print("Selamat datang di dunia coding! 👨‍💻👩‍💻")
elif jurusan == "sistem informasi":
    print("Siap menjadi penghubung antara bisnis dan teknologi!")
else:
    print("Jurusan kamu pasti keren! Tetap semangat belajar 😊")

print("======================================")
print("Program selesai.")
