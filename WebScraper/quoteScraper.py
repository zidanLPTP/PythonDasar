import requests
from bs4 import BeautifulSoup
import pandas as pd

# tentukan base url dan lihat respon yang diberikan
url = "https://quotes.toscrape.com/"
respon = requests.get(url)
respon.raise_for_status()
soup = BeautifulSoup(respon.text, "html.parser")

# buat wadah kosong tempat menyimpan hasil
list_kutipan, list_penulis, list_tag = [], [], []
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
    

# tampilkan semua
for a, b, c in zip(list_kutipan, list_penulis, list_tag):
    print(f"Kutipan: {a}\n Ditulis oleh: {b}\nTags: {c}\n")

# jadikan ke excel
convert = pd.DataFrame({
    "Kutipan:" : list_kutipan,
    "Penulis:" : list_penulis,
    "Tags:" : list_tag
})

convert.to_excel("DataQuote.xlsx", index=False)
print("data berhasil disimpan di 'DataQuote.xlsx'")