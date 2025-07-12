# ================================================
# Modul: multilevel_inheritance.py
# Konsep: Multilevel Inheritance (Pewarisan Bertingkat)
# Cocok untuk: Pemula yang ingin memahami pewarisan lanjutan di OOP
# ================================================

# ✅ Kelas paling dasar: Hewan
class Hewan:
    def __init__(self):
        self.nama = input("Nama hewan: ")
        self.jumlah_kaki = int(input("Jumlah kaki: "))
    
    def info(self):
        print("\n📄 === Info Hewan ===")
        print(f"🐾 Nama         : {self.nama}")
        print(f"🦵 Jumlah Kaki  : {self.jumlah_kaki}")

# ✅ Kelas turunan dari Hewan → Mamalia
class Mamalia(Hewan):
    def __init__(self):
        super().__init__()  # Memanggil konstruktor dari Hewan
        self.menyusui = input("Apakah hewan ini menyusui? (ya/tidak): ")

# ✅ Kelas turunan dari Mamalia → Anjing
class Anjing(Mamalia):
    def __init__(self):
        super().__init__()  # Memanggil konstruktor dari Mamalia (dan otomatis Hewan juga)
        self.ras = input("Apa ras anjing ini? ")
    
    def suara(self):
        print(f"🔊 {self.nama} menggonggong: Woof! Woof!")

    def tampilkan(self):
        # Gabungkan semua info dari atas
        self.info()
        print(f"🍼 Menyusui     : {self.menyusui}")
        print(f"🐶 Ras Anjing   : {self.ras}")
        print("===============================")


# ========================================
# Eksekusi hanya jika file ini dijalankan langsung
# ========================================
if __name__ == "__main__":
    print("📚 Demo Multilevel Inheritance - Contoh Anjing\n")

    # Membuat objek dari kelas paling bawah (Anjing)
    anjingku = Anjing()
    
    # Menampilkan seluruh data hasil pewarisan bertingkat
    anjingku.tampilkan()
    
    # Tes fungsi tambahan
    anjingku.suara()
