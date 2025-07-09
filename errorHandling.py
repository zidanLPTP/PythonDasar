print("Error Handling dalam Python")
print("=" * 40)

# Penjelasan struktur umum
# try:
#     kode yang bisa menyebabkan error
# except JenisError:
#     penanganan jika terjadi error
# else:
#     jika tidak terjadi error (opsional)
# finally:
#     selalu dijalankan (opsional)

# =========================================
# 1. Dasar: Menangani error dengan try-except
# =========================================

while True:
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        hasil = angka1 / angka2
    except Exception as e:
        print(f"Error terjadi: {e}")
        continue
    else:
        print(f"Hasil pembagian: {hasil}")
        break
    finally:
        print("Blok finally dijalankan (terlepas dari error atau tidak)")

# =========================================
# 2. Menangani banyak jenis error sekaligus
# =========================================

print("\nMenangani beberapa error:")
try:
    angka = int(input("Masukkan angka (bukan 0): "))
    hasil = 10 / angka
except (ValueError, ZeroDivisionError) as err:
    print("Terjadi kesalahan:", err)

# =========================================
# 3. Menimbulkan error secara manual dengan raise
# =========================================

print("\nContoh raise error:")
nilai = int(input("Masukkan nilai (0–100): "))
if not 0 <= nilai <= 100:
    raise ValueError("Nilai harus antara 0 dan 100!")

# =========================================
# 4. Penanganan error pada file
# =========================================

print("\nMembaca file dengan penanganan error:")
try:
    with open("file_tidak_ada.txt", "r") as f:
        isi = f.read()
except FileNotFoundError:
    print("File tidak ditemukan!")

# =========================================
# 5. Mini fungsi validasi input angka
# =========================================

print("\nValidasi input angka:")

def input_angka():
    while True:
        try:
            return int(input("Masukkan angka: "))
        except ValueError:
            print("Itu bukan angka! Coba lagi.")

a = input_angka()
b = input_angka()
print(f"Hasil penjumlahan: {a + b}")
