# ==============================
# Modul: mobil.py
# Konsep: Class, Object, Constructor (__init__), Method, Classmethod, Staticmethod
# Tujuan: Belajar dasar OOP (Object-Oriented Programming) dalam Python
# ==============================

class Mobil:
    def __init__(self, jenis, warna, desain, mesin, transmisi, harga):
        """
        Constructor untuk membuat objek Mobil.
        Menerima parameter dan menyimpannya sebagai atribut objek.
        """
        self.jenis = jenis
        self.warna = warna
        self.desain = desain
        self.mesin = mesin
        self.transmisi = transmisi
        self.harga = harga

    def menyala(self):
        """Menampilkan bahwa mobil menyala dengan jenis mesin tertentu."""
        print(f"💡 Mobil {self.jenis} menyala dengan mesin {self.mesin}.")

    def tampilkan_atribut(self):
        """Menampilkan semua atribut dari mobil ini."""
        print("\n🚗 === Detail Mobil ===")
        print("📌 Jenis Mobil     :", self.jenis)
        print("🎨 Warna Mobil     :", self.warna)
        print("🎭 Desain Mobil    :", self.desain)
        print("🔧 Mesin Mobil     :", self.mesin)
        print("⚙️  Transmisi Mobil :", self.transmisi)
        print("💰 Harga Mobil     : Rp.", format(self.harga, ","))
        print("=========================")

    @classmethod
    def dari_string(cls, data_string):
        """
        Membuat objek Mobil dari sebuah string.
        Format string: 'jenis,warna,desain,mesin,transmisi,harga'
        """
        print("\n📥 Membuat objek dari string:", data_string)
        jenis, warna, desain, mesin, transmisi, harga = data_string.split(",")
        return cls(jenis, warna, desain, mesin, transmisi, int(harga))

    @staticmethod
    def konversi_rupiah_ke_dolar(harga, kurs=15000):
        """
        Konversi harga dari rupiah ke dolar berdasarkan kurs tertentu.
        Default kurs = 15000.
        """
        return harga / kurs

    def tampilkan_harga(self, harga_dolar):
        """Menampilkan harga mobil dalam dolar dengan format yang rapi."""
        print(f"💵 Harga mobil {self.jenis}: $ {harga_dolar:,.2f}")


# ============================
# Bagian ini hanya akan berjalan jika file ini dijalankan langsung
# ============================

if __name__ == "__main__":
    print("\n🔥 Membuat Objek Mobil Secara Manual")
    mobil1 = Mobil("Sedan", "Hitam", "Elegan", "Diesel", "Manual", 500_000_000)
    mobil2 = Mobil("SUV", "Merah", "Sporty", "Bensin Turbo", "Otomatis", 750_000_000)

    # Menampilkan info mobil 1
    print("\n🛠 Menampilkan info Mobil 1:")
    print("🧾 Atribut mentah mobil1 (dictionary):", mobil1.__dict__)
    mobil1.menyala()
    mobil1.tampilkan_atribut()

    # Menampilkan info mobil 2
    print("\n🛠 Menampilkan info Mobil 2:")
    print("🧾 Atribut mentah mobil2 (dictionary):", mobil2.__dict__)
    mobil2.menyala()
    mobil2.tampilkan_atribut()

    # Membuat mobil ketiga dari string menggunakan classmethod
    print("\n✨ Membuat Objek Mobil dengan @classmethod")
    data_mobil = "Hatchback,Biru,Mungil,Bensin,Otomatis,200000000"
    mobil3 = Mobil.dari_string(data_mobil)

    # Menampilkan info mobil 3
    print("\n🛠 Menampilkan info Mobil 3:")
    print("🧾 Atribut mentah mobil3 (dictionary):", mobil3.__dict__)
    mobil3.menyala()
    mobil3.tampilkan_atribut()

    # Menampilkan harga dolar dari semua mobil
    print("\n💱 Mengkonversi Harga Mobil ke Dolar")
    for mobil in [mobil1, mobil2, mobil3]:
        harga_dolar = Mobil.konversi_rupiah_ke_dolar(mobil.harga)
        mobil.tampilkan_harga(harga_dolar)

    # Bonus interaktif sederhana (optional, bisa kamu abaikan sebagai pembaca kalau enggak mau)
    print("\n🧪 Coba input mobil kamu sendiri:")
    try:
        string_input = input("Masukkan data mobil (format: jenis,warna,desain,mesin,transmisi,harga): ")
        mobil_custom = Mobil.dari_string(string_input)
        mobil_custom.menyala()
        mobil_custom.tampilkan_atribut()
        harga_dolar = Mobil.konversi_rupiah_ke_dolar(mobil_custom.harga)
        mobil_custom.tampilkan_harga(harga_dolar)
    except Exception as e:
        print("⚠️ Format salah atau input gagal:", e)
