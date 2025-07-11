# Lesson 02: Navigating and Searching the HTML Tree in BeautifulSoup

Saat kamu melakukan web scraping, HTML dari sebuah halaman web bisa dianggap sebagai struktur pohon (tree). BeautifulSoup membuat proses navigasi dan pencarian dalam pohon ini menjadi sangat mudah.

---

## 🔹 1. Navigating Tags and Contents

### 📌 Akses Tag Langsung

```python
from bs4 import BeautifulSoup

html = "<html><head><title>Contoh Judul</title></head><body><p>Hello World!</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

print(soup.title)
```

**Output:**

```html
<title>Contoh Judul</title>
```

### 📌 Mengakses Isi Tag

```python
print(soup.title.string)
```

**Output:**

```
Contoh Judul
```

---

## 🔹 2. Navigasi Struktur HTML

### 📌 .parent → Akses Induk Tag

```python
title_tag = soup.title
print(title_tag.parent.name)
```

**Output:**

```
head
```

### 📌 .children → Akses Anak Langsung (Iterator)

```python
for child in soup.body.children:
    print(child)
```

**Output:**

```html
<p>Hello World!</p>
```

### 📌 .descendants → Semua Anak (Cucu, Cicit, dst)

```python
for desc in soup.body.descendants:
    print(desc)
```

**Output:**

```html
<p>Hello World!</p>
Hello World!
```

### 📌 .next\_sibling & .previous\_sibling

```python
html = """
<html>
  <body>
    <p>Paragraf 1</p>
    <p>Paragraf 2</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
p1 = soup.find('p')
print(p1.next_sibling)
```

**Output:**

```
\n
```

> Gunakan `.next_sibling.next_sibling` untuk melewati spasi atau newline.

---

## 🔹 3. Searching with find() dan find\_all()

### 📌 Cari Tag Pertama

```python
print(soup.find("p"))
```

**Output:**

```html
<p>Paragraf 1</p>
```

### 📌 Cari Semua Tag Tertentu

```python
all_p = soup.find_all("p")
for p in all_p:
    print(p.text)
```

**Output:**

```
Paragraf 1
Paragraf 2
```

### 📌 Cari Berdasarkan Atribut

```python
html = '<div class="content">Isi konten</div>'
soup = BeautifulSoup(html, "html.parser")
print(soup.find("div", {"class": "content"}))
```

**Output:**

```html
<div class="content">Isi konten</div>
```

---

## 🔹 4. Searching Menggunakan CSS Selectors

### 📌 `select_one()` dan `select()`

```python
html = '<div class="content"><p class="intro">Hai</p><ul><li>1</li><li>2</li></ul></div>'
soup = BeautifulSoup(html, "html.parser")

print(soup.select_one(".intro").text)
```

**Output:**

```
Hai
```

```python
list_items = soup.select("div.content li")
for li in list_items:
    print(li.text)
```

**Output:**

```
1
2
```

---

## 🔹 5. Text-Based Search

```python
html = "<p>Belajar Python itu menyenangkan</p>"
soup = BeautifulSoup(html, "html.parser")

hasil = soup.find_all(text="Python")
print(hasil)
```

**Output:**

```
['Belajar Python itu menyenangkan']
```

---

## 🔹 6. Pencarian dengan Regex

```python
import re

html = """
<h1>Judul</h1>
<h2>Subjudul</h2>
<h3>Sekilas</h3>
"""
soup = BeautifulSoup(html, "html.parser")

header_tags = soup.find_all(re.compile("^h[1-3]$"))
for h in header_tags:
    print(h.text)
```

**Output:**

```
Judul
Subjudul
Sekilas
```

---

## 📉 Tabel Ringkasan Fungsi Navigasi

| ---------------------- | ----------------------------------------- |
| Fungsi/Properti        | Keterangan Singkat                        |
| ---------------------- | ----------------------------------------- |
| `tag.parent`           | Akses ke induk tag                        |
| `tag.children`         | Iterator ke anak langsung                 |
| `tag.descendants`      | Semua keturunan (anak, cucu, dst)         |
| `tag.next_sibling`     | Elemen setelahnya (bisa `\n`)             |
| `tag.previous_sibling` | Elemen sebelum tag                        |
| `find()`               | Temukan 1 tag                             |
| `find_all()`           | Temukan semua tag                         |
| `select()`             | Temukan dengan CSS selector               |
| `select_one()`         | Sama seperti `select()`, tapi satu elemen |
| `text="..."`           | Cari berdasarkan isi teks                 |
| `re.compile(...)`      | Pencarian menggunakan regex               |
| ---------------------- | ----------------------------------------- |

---