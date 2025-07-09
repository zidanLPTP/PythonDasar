import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL target scraping
link_dasar = "https://jobindo.com/lowongan-kerja-terbaru.html"

# Mengirim permintaan HTTP GET ke URL
minta_status = requests.get(link_dasar)

# Parsing HTML-nya menggunakan BeautifulSoup
soup = BeautifulSoup(minta_status.text, "html.parser")

# Ambil data nama pekerjaan
job_title = soup.find_all("h4", class_="results-job-title")
list_judul = [judul.text.strip() for judul in job_title]

# Ambil data nama PT
pt_title = soup.find_all("font", class_="no-margin")
list_pt = [pt.text.strip() for pt in pt_title]

# Ambil data lokasi
td_tags = soup.find_all('td')
strong_texts = []

for td in td_tags:
    strong = td.find('strong')
    if strong:
        text = strong.get_text(strip=True)
        if ',' in text:
            parts = text.split(',')
            if len(parts) == 2:
                strong_texts.append(text)

# Print hasil yang didapatkan
# for judul, pt, lokasi in zip(list_judul, list_pt, strong_texts):
#     print(f"Dicari: {judul} \nDari PT: {pt} \nLokasi: {lokasi}\n")

# panjang tidak sama, solusi pakai min()
# print("Jumlah judul:", len(list_judul))
# print("Jumlah PT:", len(list_pt))
# print("Jumlah lokasi:", len(strong_texts))

min_len = min(len(list_judul), len(list_pt), len(strong_texts))

excel = pd.DataFrame({
    "Dicari:": list_judul[:min_len],
    "PT:": list_pt[:min_len],
    "Lokasi:": strong_texts[:min_len]
})

excel.to_excel("DataJobindo.xlsx", index=False)
print("Data berhasil disimpan ke DataJobindo.xlsx")
