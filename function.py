print("FUNGSI DALAM PYTHON")
print("="*40)

# ~ 1. Pengantar Fungsi
print("\n~ Membuat fungsi sederhana")
def sapa():
    print("Halo! Selamat datang belajar Python.")

sapa()

# ~ 2. Fungsi dengan parameter
print("\n~ Fungsi dengan parameter")
def halo_nama(nama):
    print("Halo,", nama)

halo_nama("Zidan")

# ~ 3. Fungsi dengan return
print("\n~ Fungsi dengan return")
def kali(a, b):
    return a * b

hasil = kali(5, 3)
print("Hasil perkalian 5 x 3 =", hasil)

# ~ 4. Fungsi dengan default value
print("\n~ Fungsi dengan parameter default")
def sapa_default(nama="Anonim"):
    print("Halo,", nama)

sapa_default()
sapa_default("Rina")

# ~ 5. Fungsi dengan banyak argumen (*args)
print("\n~ Fungsi dengan *args (argumen tak terbatas)")
def jumlahkan(*angka):
    total = 0
    for i in angka:
        total += i
    return total

print("Jumlah dari 1,2,3,4 =", jumlahkan(1,2,3,4))

# ~ 6. Fungsi dengan keyword args (**kwargs)
print("\n~ Fungsi dengan **kwargs (parameter kunci)")
def biodata(**data):
    for key, val in data.items():
        print(f"{key} : {val}")
        
biodata(nama="Zidan", umur=20, status="Pelajar")

print("\n~ modul untuk import")
print("="*40)

def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi(a,b):
    return a / b