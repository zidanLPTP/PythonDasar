# ============================
# 🧪 MODUL PEMBELAJARAN ASSERT DI PYTHON
# ============================

print("========== MODUL PEMBELAJARAN `assert` ==========")
print("📌 `assert` adalah statement bawaan Python untuk mengecek apakah suatu kondisi benar.")
print("📌 Jika kondisi salah (False), maka program akan error dengan AssertionError.")
print("📌 Ini sering dipakai saat debugging, atau dalam testing otomatis seperti pytest.")
print("=" * 50)


# ============================
# ✅ CONTOH 1: assert benar
# ============================
print("\n✅ Contoh 1: Kondisi assert yang BENAR")

nilai = 80
print(f"Nilai = {nilai}")
assert nilai >= 70  # kondisi benar
print("✅ Assert berhasil: nilai >= 70")


# ============================
# ❌ CONTOH 2: assert salah
# ============================
print("\n❌ Contoh 2: Kondisi assert yang SALAH")

umur = 15
print(f"Umur = {umur}")
print("Sekarang kita cek: assert umur >= 17 (harusnya gagal)")

try:
    assert umur >= 17
except AssertionError:
    print("❌ Assert gagal: Umur kurang dari 17 (AssertionError muncul)")


# ============================
# 💡 CONTOH 3: assert dengan pesan khusus
# ============================
print("\n💡 Contoh 3: assert dengan pesan keterangan")

angka = 5
print(f"Angka = {angka}")
try:
    assert angka > 10, "Angka harus lebih dari 10"
except AssertionError as e:
    print(f"❌ Assert gagal: {e}")


# ============================
# 📦 CONTOH 4: Fungsi cek login dengan assert
# ============================
print("\n📦 Contoh 4: Fungsi validasi login sederhana pakai assert")


def login(username, password):
    assert username != "", "Username tidak boleh kosong"
    assert password != "", "Password tidak boleh kosong"
    print("✅ Login berhasil!")


# Coba login dengan data benar
print(">> Test login dengan data benar")
login("zidan", "123456")

# Coba login dengan username kosong
print(">> Test login dengan username kosong")
try:
    login("", "123456")
except AssertionError as e:
    print(f"❌ Gagal login: {e}")
