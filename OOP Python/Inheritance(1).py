# =========================================
# Modul: inheritance_only.py
# Fokus Pembelajaran: PURE INHERITANCE
# Tanpa: Polymorphism, Encapsulation
# =========================================
# Modul ini ditujukan untuk pemula yang ingin memahami konsep pewarisan (inheritance)
# secara murni di OOP Python tanpa tambahan pilar lain.
# =========================================

# 👉 Kelas induk / parent class
class Kendaraan:
    def __init__(self):
        # Setiap objek kendaraan akan meminta input atribut dasar
        self.nama = input("Nama kendaraan: ")
        self.roda = int(input("Jumlah roda: "))
        self.penumpang = int(input("Maksimal penumpang: "))

    def info(self):
        # Fungsi untuk menampilkan info dasar kendaraan
        print("\n=== Info Kendaraan ===")
        print(f"Nama         : {self.nama}")
        print(f"Roda         : {self.roda}")
        print(f"Penumpang    : {self.penumpang}")


# 👉 Subclass Mobil yang mewarisi dari Kendaraan
class Mobil(Kendaraan):
    def __init__(self):
        super().__init__()  # Memanggil constructor dari parent (Kendaraan)
        # Menambahkan atribut khusus untuk mobil
        self.pintu = int(input("Jumlah pintu mobil: "))
        self.bagasi = input("Apakah ada bagasi? (ya/tidak): ")


# 👉 Subclass Motor yang mewarisi dari Kendaraan
class Motor(Kendaraan):
    def __init__(self):
        super().__init__()  # Mewarisi konstruktor dari Kendaraan
        # Menambahkan atribut unik untuk motor
        self.knalpot = input("Jenis knalpot: ")


# 👉 Subclass Bus yang mewarisi dari Kendaraan
class Bus(Kendaraan):
    def __init__(self):
        super().__init__()  # Memanggil konstruktor parent
        # Menambahkan properti spesifik bus
        self.tingkat = input("Apakah bus tingkat? (ya/tidak): ")
        self.kelas = input("Kelas bus: ")


# =========================================
# Blok ini hanya akan dijalankan jika file ini
# dijalankan langsung, bukan saat di-import sebagai modul.
# =========================================
if __name__ == "__main__":
    print("🎯 DEMO PROGRAM: Pewarisan (Inheritance) di Python\n")

    print("🔧 [1] Objek Mobil:")
    mobil = Mobil()              # Membuat objek Mobil
    mobil.info()                 # Memanggil fungsi dari parent class
    print(f"Jumlah Pintu : {mobil.pintu}")
    print(f"Bagasi       : {mobil.bagasi}")

    print("\n🏍️ [2] Objek Motor:")
    motor = Motor()              # Membuat objek Motor
    motor.info()
    print(f"Jenis Knalpot: {motor.knalpot}")

    print("\n🚌 [3] Objek Bus:")
    bus = Bus()                  # Membuat objek Bus
    bus.info()
    print(f"Tingkat      : {bus.tingkat}")
    print(f"Kelas        : {bus.kelas}")

    print("\n✅ Semua objek berhasil dibuat dan ditampilkan.")