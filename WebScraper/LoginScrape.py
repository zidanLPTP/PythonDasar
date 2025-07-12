import requests
from bs4 import BeautifulSoup

# Buat session
session = requests.Session()

# Tambahkan header
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

# URL halaman login
base_url = "https://quotes.toscrape.com/login"

# Buka halaman login untuk ambil token
login_page = session.get(base_url)
soup_login = BeautifulSoup(login_page.text, "html.parser")

# Ambil token CSRF
csrf_input = soup_login.find("input", {"name": "csrf_token"})
if csrf_input:
    csrf_token = csrf_input["value"]
else:
    raise Exception("⚠️ CSRF token tidak ditemukan!")

# Data login
data_login = {
    "csrf_token": csrf_token,
    "username": "admin",
    "password": "admin"
}

# Kirim POST login
login_response = session.post(base_url, data=data_login)

# Akses halaman utama
respon = session.get("https://quotes.toscrape.com/")
respon.raise_for_status()

# Verifikasi login berhasil
if "Logout" in respon.text:
    print("✅ Login berhasil!")
    soup = BeautifulSoup(respon.text, "html.parser")
    print("Judul halaman:", soup.title.string)
    quote = soup.find("span", class_="text").text
    print("Kutipan pertama:", quote)
else:
    print("❌ Login gagal. Cek username/password atau token.")