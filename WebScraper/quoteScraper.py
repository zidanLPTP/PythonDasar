import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# tentukan base url dan halaman akan berubah
url = "https://quotes.toscrape.com/"
halaman_scrape = url

# buat wadah kosong tempat menyimpan hasil
list_kutipan, list_penulis, list_tag = [], [], []

# loop terus selama punya halaman
while halaman_scrape:
    print(f"Halaman scrape ke-{halaman_scrape}")

    respon = requests.get(halaman_scrape)
    print(respon)
    respon.raise_for_status()
    soup = BeautifulSoup(respon.text, "html.parser")

    semua_kutipan = soup.find_all("div", class_="quote")

    for isi in semua_kutipan:
        kutipan = isi.find("span", class_="text").text
        list_kutipan.append(kutipan)

        penulis = isi.find("small", class_="author").text
        list_penulis.append(penulis)

        kontainer_tag = isi.find("div", class_="tags")
        isi_tag = kontainer_tag.find_all("a", class_="tag")
        # gabungkan semua isi dengan koma sebagai pemisah
        final_tag = ", ".join(tag.text for tag in isi_tag)
        list_tag.append(final_tag)
        
    # fungsi terus ke halaman selanjutnya
    next_li = soup.find("li", class_="next")

    # Jika elemen 'next' ditemukan, buat URL lengkap untuk halaman berikutnya
    if next_li:
        # Ambil link relatif (contoh: /page/2/) dari tag <a> di dalamnya
        next_page_relative_url = next_li.find("a")["href"]
        # Gabungkan base_url dengan link relatif untuk dapat URL lengkap
        url_to_scrape = urljoin(url, next_page_relative_url)
        # Selalu update next hal
        halaman_scrape = url_to_scrape
    else:
        # Jika tidak ada elemen 'next', kita di halaman terakhir. Hentikan loop.
        halaman_scrape = None

# tampilkan semua
for a, b, c in zip(list_kutipan, list_penulis, list_tag):
    print(f"Kutipan: {a}\n Ditulis oleh: {b}\nTags: {c}\n")

print("Scraping selesai... menyimpan data")

# jadikan ke excel
convert = pd.DataFrame({
    "Kutipan:" : list_kutipan,
    "Penulis:" : list_penulis,
    "Tags:" : list_tag
})

convert.to_excel("DataQuote.xlsx", index=False)
print("data berhasil disimpan di 'DataQuote.xlsx'")