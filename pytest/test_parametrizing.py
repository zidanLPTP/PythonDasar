import pytest

print("🔍 Modul: Belajar Pytest Parameterizing untuk Pemula")
print("-----------------------------------------------------")
print("✅ Kita bisa mengetes satu fungsi dengan banyak data sekaligus pakai @pytest.mark.parametrize")
print("✅ Pytest akan otomatis mengulang test sebanyak jumlah data yang diberikan")
print("-----------------------------------------------------\n")

# Fungsi yang akan kita tes
def kali(a, b):
    return a * b

# Parameterized test: akan dijalankan 4x dengan data berbeda
@pytest.mark.parametrize(
    "a, b, expected", [
        (2, 3, 6),     # ✅ PAS
        (5, 0, 0),     # ✅ PAS
        (-1, 8, -8),   # ✅ PAS
        (3, 4, 13),    # ❌ SALAH (seharusnya 12) → Biar ada test yang gagal
    ]
)
def test_kali(a, b, expected):
    print(f"Menguji kali({a}, {b})... Harusnya: {expected}")
    assert kali(a, b) == expected


# Fungsi lain: pembagian
def bagi(x, y):
    return x / y

@pytest.mark.parametrize(
    "x, y, expected", [
        (10, 2, 5),     # ✅
        (9, 3, 3),      # ✅
        (5, 2, 10),   # ❌ (akan raise ZeroDivisionError)
    ]
)
def test_bagi(x, y, expected):
    print(f"Menguji bagi({x}, {y})... Harusnya: {expected}")
    assert bagi(x, y) == expected 
