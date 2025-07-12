# ============================================
# Modul: akses_inheritance.py
# Topik: Public, Protected, Private + Getter & Setter
# ============================================

class Manusia:
    def __init__(self, nama, umur, gaji):
        self.nama = nama              # Public
        self._umur = umur             # Protected
        self.__gaji = gaji            # Private

    def tampilkan_data(self):
        print(f"Nama (public): {self.nama}")
        print(f"Umur (protected): {self._umur}")
        print(f"Gaji (private): {self.__gaji}")

    # 🔓 GETTER untuk gaji (akses aman terhadap private)
    def get_gaji(self):
        return self.__gaji

    # 🔒 SETTER untuk gaji (ubah nilai private dengan validasi jika perlu)
    def set_gaji(self, nilai_baru):
        if nilai_baru > 0:
            self.__gaji = nilai_baru
            print("✅ Gaji berhasil diubah.")
        else:
            print("❌ Gaji tidak boleh negatif!")

# Subclass
class Karyawan(Manusia):
    def __init__(self, nama, umur, gaji, jabatan):
        super().__init__(nama, umur, gaji)
        self.jabatan = jabatan

    def akses_data(self):
        print("\n📌 Akses dari dalam subclass:")
        print(f"Nama (public): {self.nama}")       # ✅ Public
        print(f"Umur (protected): {self._umur}")   # ✅ Protected
        print(f"Gaji (private, via getter): {self.get_gaji()}")  # ✅ Akses pakai getter

if __name__ == "__main__":
    orang = Manusia("Andi", 30, 10_000_000)
    print("🔍 Akses dari luar class:")
    print(orang.nama)         # ✅ Public
    print(orang._umur)        # ⚠️ Protected
    # print(orang.__gaji)     # ❌ Private, error!

    orang.tampilkan_data()

    # 🔧 Akses dan ubah private attribute dengan getter & setter
    print("\n💰 Gaji asli:", orang.get_gaji())
    orang.set_gaji(12_000_000)
    print("💵 Gaji baru:", orang.get_gaji())

    print("\n==== Subclass ====")
    pegawai = Karyawan("Budi", 28, 8_000_000, "Staff")
    pegawai.akses_data()
    pegawai.set_gaji(9_000_000)  # Gunakan setter dari parent
    print("💼 Gaji baru setelah kenaikan:", pegawai.get_gaji())