# ==============================================
# Modul: polymorphism.py
# Topik: Polymorphism dalam OOP Python
# ==============================================
# Dua bentuk utama:
# 1. Polymorphism dengan inheritance (method overriding)
# 2. Polymorphism tanpa inheritance (duck typing)
# ==============================================

# 🐾 POLYMORPHISM VIA INHERITANCE (METHOD OVERRIDING)
class Hewan:
    def bersuara(self):
        print("Hewan ini mengeluarkan suara...")

class Kucing(Hewan):  # 🔄 override method
    def bersuara(self):
        print("🐱 Meong~")

class Anjing(Hewan):  # 🔄 override method
    def bersuara(self):
        print("🐶 Guk-guk!")

# Fungsi yang menggunakan polymorphism
def tes_suara(hewan):
    # ⛅ Method polymorphic: tergantung objek yang dikirim
    hewan.bersuara()


# 🐤 POLYMORPHISM VIA DUCK TYPING (tanpa inheritance)
class Robot:
    def bersuara(self):
        print("🤖 Beep bop...")

class Burung:
    def bersuara(self):
        print("🕊️  Cuit-cuit~")

def tes_duck_typing(objek):
    # Python tidak peduli dari class mana objek berasal
    # Asal punya method `bersuara`, maka akan jalan
    objek.bersuara()


# ==============================
# Eksekusi utama
# ==============================
if __name__ == "__main__":
    print("📦 Contoh 1: Polymorphism via Inheritance")
    hewan1 = Kucing()
    hewan2 = Anjing()

    tes_suara(hewan1)  # Output: Meong~
    tes_suara(hewan2)  # Output: Guk-guk!

    print("\n📦 Contoh 2: Duck Typing (tanpa inheritance)")
    objek1 = Robot()
    objek2 = Burung()

    tes_duck_typing(objek1)  # Output: Beep bop...
    tes_duck_typing(objek2)  # Output: Cuit-cuit~
