import datetime

print("Belajar Modul datetime untuk Pemula")
print("======================================")

# ~ 1. Menampilkan tanggal dan waktu sekarang
sekarang = datetime.datetime.now()
print("\n1. Sekarang:")
print("Tanggal dan waktu sekarang :", sekarang)

# ~ 2. Menampilkan hanya tanggal hari ini (tanpa jam)
hari_ini = datetime.date.today()
print("\n2. Tanggal hari ini:", hari_ini)

# ~ 3. Membuat tanggal secara manual
tanggal_lahir = datetime.date(2005, 9, 20)
print("\n3. Tanggal lahir yang dibuat manual:", tanggal_lahir)

# ~ 4. Mengambil bagian dari tanggal
print("\n4. Mengakses bagian tahun, bulan, hari:")
print("   Tahun :", hari_ini.year)
print("   Bulan :", hari_ini.month)
print("   Hari  :", hari_ini.day)

# ~ 5. Menghitung selisih dua tanggal (hitung umur, countdown, dsb)
umur = hari_ini - tanggal_lahir
print("\n5. Umur dalam hari:", umur.days, "hari")

# ~ 6. Menambah atau mengurangi hari (dengan timedelta)
besok = hari_ini + datetime.timedelta(days=1)
kemarin = hari_ini - datetime.timedelta(days=1)
print("\n6. Tambah/Kurang Hari:")
print("   Besok   :", besok)
print("   Kemarin :", kemarin)

# ~ 7. Format tanggal ke string (contoh: "Senin, 07 Juli 2025")
format_tanggal = sekarang.strftime("%A, %d %B %Y")
print("\n7. Format tanggal yang rapi:")
print("   Hari ini adalah:", format_tanggal)
