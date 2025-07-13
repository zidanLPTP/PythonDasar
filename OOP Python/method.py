# ==================================================
# Modul: semua_method_oop.py
# Topik: Kombinasi semua jenis method di Python
# Termasuk: instance method, classmethod, staticmethod, abstractmethod
# Cocok untuk: Belajar OOP Python tingkat lanjut pemula
# ==================================================

from abc import ABC, abstractmethod

# === Abstract Base Class ===
class Karyawan(ABC):
    total_karyawan = 0  # ➕ Atribut class (untuk classmethod)

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.total_karyawan += 1

    def info(self):  # ✅ Instance method
        print(f"Nama: {self.nama}")
        print(f"Gaji: Rp{self.gaji:,}")

    @classmethod
    def jumlah_karyawan(cls):  # ✅ Classmethod
        print(f"Jumlah total karyawan: {cls.total_karyawan}")

    @staticmethod
    def format_rupiah(angka):  # ✅ Staticmethod
        return f"Rp{angka:,.2f}"

    @abstractmethod
    def tugas(self):  # ✅ Abstractmethod (wajib di subclass)
        pass

# === Subclass: Programmer ===
class Programmer(Karyawan):
    def __init__(self, nama, gaji, bahasa):
        super().__init__(nama, gaji)
        self.bahasa = bahasa

    def tugas(self):  # 🔄 Wajib override abstractmethod
        print(f"{self.nama} membuat aplikasi dengan {self.bahasa}")

# === Subclass: Desainer ===
class Desainer(Karyawan):
    def __init__(self, nama, gaji, tools):
        super().__init__(nama, gaji)
        self.tools = tools

    def tugas(self):
        print(f"{self.nama} mendesain dengan tools {self.tools}")

# ==================================================
# Eksekusi utama
# ==================================================
if __name__ == "__main__":
    print("👥 Membuat objek karyawan dari dua role:\n")

    # Programmer
    p1 = Programmer("Zidan", 10_000_000, "Python")
    p1.info()
    p1.tugas()
    print("Format gaji:", Karyawan.format_rupiah(p1.gaji))  # Static method

    print("\n-----------------------------\n")

    # Desainer
    d1 = Desainer("Nisa", 9_000_000, "Figma")
    d1.info()
    d1.tugas()
    print("Format gaji:", Karyawan.format_rupiah(d1.gaji))  # Static method

    print("\n📊 Rekap karyawan:")
    Karyawan.jumlah_karyawan()  # Class method