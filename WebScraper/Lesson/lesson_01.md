# Lesson 01: Introduction to Web Scraping and BeautifulSoup

Web scraping adalah teknik untuk mengambil data dari situs web secara otomatis. Dalam pelajaran ini, kamu akan mempelajari dasar-dasar web scraping dengan Python dan BeautifulSoup, sebuah library populer yang sangat cocok untuk pemula.

---

## 🔹 Apa Itu Web Scraping?

Web scraping adalah proses mengambil data dari halaman web. Saat kamu membuka situs, browser akan menerima konten HTML. Scraper memungkinkan kita mengambil data itu tanpa membuka browser.

### 📌 Contoh Penggunaan Web Scraping:

- Mengambil data harga dari e-commerce.
- Kumpulan artikel atau berita.
- Pemantauan review pelanggan.
- Pengumpulan data riset akademis.

---

## 🔹 Tantangan Web Scraping

| Tantangan      | Penjelasan                                         |
| -------------- | -------------------------------------------------- |
| Legalitas      | Beberapa situs melarang scraping di ToS mereka.    |
| Konten Dinamis | Banyak situs pakai JavaScript untuk load data.     |
| IP Blocking    | Situs bisa memblokir jika ada trafik mencurigakan. |

---

## 🔹 Pengenalan BeautifulSoup

BeautifulSoup adalah library Python untuk mengambil data dari HTML/XML. Bersama `requests`, kita bisa scraping halaman web statis.

### Instalasi:

```bash
pip install beautifulsoup4 requests
```

---

## 🔹 Contoh Scraping Sederhana

### Tujuan: Mengambil title dari sebuah halaman web

```python
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

page_title = soup.title.text
print('Page Title:', page_title)
```

### Output:

```
Page Title: Example Domain
```

---

## 🔹 Fungsi Dasar BeautifulSoup

### 1. Cari Tag Berdasarkan Nama

```python
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
```

**Output: URL yang ada di halaman**

### 2. Menggunakan CSS Selector

```python
element = soup.select_one('div.content > p')
print(element.text)
```

### 3. Mengambil Atribut Tag

```python
first_link = soup.find('a')
print(first_link['href'])
```

---

## 🔹 Penanganan Konten Dinamis

BeautifulSoup hanya membaca HTML statis. Kalau data muncul karena JavaScript (misal scroll ke bawah dulu baru muncul), kamu butuh tools tambahan seperti:

- Selenium (simulasi browser)
- Scrapy (framework scraping advance)

---

## 🔹 Studi Kasus: Scrape Blog Post

```python
import requests
from bs4 import BeautifulSoup

url = 'https://exampleblog.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Mengambil semua judul postingan
titles = soup.find_all('h2', class_='post-title')
for title in titles:
    print(title.text)
```

### Output (simulasi):

```
Cara Belajar Python
Tips Web Developer
Review Buku Machine Learning
```

---

## 📘 Ringkasan

| Fitur                     | Fungsi                                          |
| ------------------------- | ----------------------------------------------- |
| `soup.title`              | Ambil title dari HTML                           |
| `find() / find_all()`     | Cari tag tertentu berdasarkan nama atau atribut |
| `select() / select_one()` | Cari dengan CSS Selector                        |
| `.text` atau `.string`    | Ambil isi teks dari tag                         |
| `get('href')`             | Ambil atribut seperti href dari tag             |

---

> Cocok untuk dimasukkan dalam modul Web Scraping Dasar. Materi ini bisa jadi bagian pengantar sebelum lanjut ke struktur navigasi HTML di Lesson 02.

Siap lanjut ke Lesson 02? 😎

