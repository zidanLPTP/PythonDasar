# Import library eksternal yang dibutuhkan
import requests                      # Untuk mengambil konten HTML dari web
from bs4 import BeautifulSoup        # Untuk parsing dan mengambil data dari HTML
import pandas as pd                  # Untuk menyusun dan mengekspor data ke Excel

# URL target yang ingin di-scrape
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

# Mengirim permintaan HTTP GET ke URL
req = requests.get(url)

# Jika response status [200] berarti request berhasil dan bisa diolah
# Parsing HTML-nya menggunakan BeautifulSoup dengan parser bawaan dari Python
soup = BeautifulSoup(req.text, "html.parser")

# Mengambil semua elemen <a> dengan class "title" (judul produk)
titles = soup.find_all("a", class_="title")

# Mengambil semua elemen <h4> dengan class "price" (harga produk)
prices = soup.find_all("h4", class_="price")

# Mengambil semua elemen <p> dengan class "review-count float-end" (jumlah review/viewers)
reviews = soup.find_all("p", class_="review-count float-end")

# Menyusun list berisi teks bersih dari elemen HTML hasil scraping
list_judul = [judul.text.strip() for judul in titles]
list_harga = [harga.text.strip() for harga in prices]
list_review = [view.text.strip() for view in reviews]

# Membuat DataFrame dari hasil list yang sudah diproses
pf = pd.DataFrame({
    "Judul" : list_judul,
    "Harga" : list_harga,
    "Total view" : list_review
})

# Mengekspor DataFrame ke file Excel dengan nama "Hasil_Scraping_laptop.xlsx"
pf.to_excel("Hasil_Scraping_laptop.xlsx", index=False)

# Menampilkan DataFrame di terminal (opsional)
print(pf)
