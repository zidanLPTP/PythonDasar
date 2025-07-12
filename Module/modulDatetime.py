import datetime
import pytz  # Tambahan: modul timezone

print("Belajar Modul datetime + pytz untuk Pemula")
print("===========================================")

# ~ 1. Menampilkan waktu sekarang (timezone-aware) di zona lokal
zona_jakarta = pytz.timezone('Asia/Jakarta')
sekarang = datetime.datetime.now(zona_jakarta)
print("\n1. Sekarang (Jakarta):")
print("Tanggal dan waktu sekarang :", sekarang)

# ~ 2. Menampilkan hanya tanggal hari ini (tanpa jam)
hari_ini = sekarang.date()
print("\n2. Tanggal hari ini:", hari_ini)

# ~ 3. Membuat tanggal secara manual (naive)
tanggal_lahir = datetime.date(2005, 9, 20)
print("\n3. Tanggal lahir yang dibuat manual:", tanggal_lahir)

# ~ 4. Mengambil bagian dari tanggal
print("\n4. Mengakses bagian tahun, bulan, hari:")
print("   Tahun :", hari_ini.year)
print("   Bulan :", hari_ini.month)
print("   Hari  :", hari_ini.day)

# ~ 5. Menghitung selisih dua tanggal (misalnya: umur dalam hari)
umur = hari_ini - tanggal_lahir
print("\n5. Umur dalam hari:", umur.days, "hari")

# ~ 6. Menambah/mengurangi hari dengan timedelta
besok = hari_ini + datetime.timedelta(days=1)
kemarin = hari_ini - datetime.timedelta(days=1)
print("\n6. Tambah/Kurang Hari:")
print("   Besok   :", besok)
print("   Kemarin :", kemarin)

# ~ 7. Format tanggal ke string (timezone-aware)
format_tanggal = sekarang.strftime("%A, %d %B %Y")
print("\n7. Format tanggal yang rapi:")
print("   Hari ini adalah:", format_tanggal)

# ~ 8. Konversi waktu Jakarta ke zona lain (misal New York)
zona_newyork = pytz.timezone('America/New_York')
waktu_newyork = sekarang.astimezone(zona_newyork)
print("\n8. Waktu di zona lain (New York):")
print("   Jakarta :", sekarang.strftime("%d/%m/%Y %H:%M:%S"))
print("   New York:", waktu_newyork.strftime("%d/%m/%Y %H:%M:%S"))

# ~ 9. Menampilkan waktu UTC
utc_now = datetime.datetime.now(pytz.utc)
print("\n9. Waktu UTC sekarang:", utc_now.strftime("%d/%m/%Y %H:%M:%S UTC"))

# ~ 10. Menampilkan daftar timezone populer
print("\n10. Contoh zona waktu populer:")
# print(pytz.all_timezones) menampilkan semua list waktu
contoh_zona = ['Asia/Jakarta', 'America/New_York', 'Europe/London', 'Asia/Tokyo']
for zona in contoh_zona:
    z = pytz.timezone(zona)
    now = datetime.datetime.now(z)
    print(f"   {zona:20} => {now.strftime('%H:%M:%S')}")
