import pytest
import sys

# Penjelasan umum di awal
print("=== BELAJAR PYTEST.MARK ===")
print("""
Marker di pytest digunakan untuk menandai atau memberi label pada test case.
Fungsinya:
✅ Mengelompokkan test
✅ Mengontrol eksekusi test (dilewati, diparameterisasi, dll)
""")

# ===========================================
# ✅ Marker Resmi (Built-in Pytest Markers)
# ===========================================

# 1. pytest.mark.skip
print("\n🔹 Contoh 1: @pytest.mark.skip → Melewati test tanpa dijalankan")
@pytest.mark.skip(reason="Masih dalam pengembangan")
def test_dilewati():
    assert 1 == 1

# 2. pytest.mark.skipif
print("🔹 Contoh 2: @pytest.mark.skipif → Melewati test jika kondisi terpenuhi")
@pytest.mark.skipif(sys.platform == "win32", reason="Tidak dijalankan di Windows")
def test_hanya_linux():
    assert True

# 3. pytest.mark.xfail
print("🔹 Contoh 3: @pytest.mark.xfail → Menandai test yang diharapkan gagal")
@pytest.mark.xfail(reason="Fitur belum stabil")
def test_gagal_tapi_ok():
    assert 2 * 2 == 5

# 4. pytest.mark.parametrize
print("🔹 Contoh 4: @pytest.mark.parametrize → Menjalankan test dengan banyak input")
@pytest.mark.parametrize("x, y, hasil", [
    (1, 2, 3),
    (5, 5, 10),
    (2, 2, 5)  # Akan gagal
])
def test_tambah(x, y, hasil):
    assert x + y == hasil


# =================================================
# ✅ Custom Marker (harus didaftarkan di pytest.ini)
# =================================================
print("\n🔹 Contoh 5: Marker Custom → Harus didaftarkan di pytest.ini")

@pytest.mark.latihan
def test_custom_marker():
    assert "zidan".capitalize() == "Zidan"


# =====================
# 🧪 Penutup & Petunjuk
# =====================
print("""
===========================
📌 Petunjuk Menjalankan Test
===========================

1. Jalankan semua test:
   ▶ pytest modul_pytest_mark.py

2. Jalankan test spesifik:
   ▶ pytest modul_pytest_mark.py::test_tambah

3. Jalankan berdasarkan marker:
   ▶ pytest -m latihan
   (Contoh menjalankan test yang diberi marker @pytest.mark.latihan)

4. Gunakan verbose biar lebih jelas hasil test:
   ▶ pytest -v modul_pytest_mark.py

===========================
📌 Menambahkan Custom Marker
===========================

Buat file bernama `pytest.ini` di folder yang sama, lalu isi:

[pytest]
markers =
    latihan: contoh marker khusus untuk latihan belajar pytest
""")
