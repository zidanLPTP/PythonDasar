# =========================================
# Modul: error_handling_traceback.py
# Topik: Exception Handling + traceback
# =========================================

import traceback  # ✅ Library untuk melihat jejak error detail (stack trace)

print("📘 Error Handling + traceback dalam Python")
print("=" * 50)

# =============================================
# 1. Dasar try-except (masih tetap seperti sebelumnya)
# =============================================
print("\n#1 👉 Dasar try-except:")
while True:
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        hasil = angka1 / angka2
    except Exception as e:
        print(f"❌ Error terjadi: {e}")
        continue
    else:
        print(f"✅ Hasil pembagian: {hasil}")
        break
    finally:
        print("🔁 Finally block tetap dijalankan.")

# =============================================
# 2. Penanganan error dengan traceback (🔥 FOKUS DI SINI)
# =============================================
print("\n#2 👉 Menangani error dengan traceback:")

try:
    print("Simulasi error: pembagian dengan nol.")
    x = 10 / 0
except Exception as e:
    print("⚠️ Terjadi error!")
    traceback.print_exc()  # ✅ Cetak detail error lengkap ke konsol
    # Bisa juga disimpan ke file log dengan: traceback.print_exc(file=mylog)

# =============================================
# 3. Raise error manual tetap bisa
# =============================================
print("\n#3 👉 Raise error manual:")
nilai = int(input("Masukkan nilai (0–100): "))
if not 0 <= nilai <= 100:
    raise ValueError("❗ Nilai harus antara 0 dan 100!")

# =============================================
# 4. Penanganan file
# =============================================
print("\n#4 👉 Baca file dengan error handling:")
try:
    with open("file_tidak_ada.txt", "r") as f:
        isi = f.read()
except FileNotFoundError as e:
    print("📁 File tidak ditemukan!")
    traceback.print_exc()  # ✅ Tampilkan log error lengkap

# =============================================
# 5. Fungsi input aman
# =============================================
print("\n#5 👉 Fungsi input angka dengan validasi:")

def input_angka():
    while True:
        try:
            return int(input("Masukkan angka: "))
        except ValueError:
            print("⚠️ Bukan angka! Coba lagi.")

a = input_angka()
b = input_angka()
print(f"Hasil penjumlahan: {a + b}")
