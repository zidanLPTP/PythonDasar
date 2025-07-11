# Lesson 03: Working with BeautifulSoup Parsers

Saat menggunakan BeautifulSoup, kamu harus memilih "parser" untuk membaca HTML/XML. Parser akan membentuk struktur pohon (DOM Tree) dari HTML sehingga kamu bisa navigasi dan ambil data.

BeautifulSoup mendukung beberapa parser dengan kelebihan dan kekurangannya masing-masing. Yuk kita pelajari satu per satu!

---

## 🔹 Apa Itu Parser?

Parser membaca dokumen HTML/XML dan mengubahnya menjadi struktur pohon (tree) agar mudah dianalisis. BeautifulSoup mendukung:

|----------------|--------------|----------------|-------------------------------|
| Parser         | Jenis Konten | Perlu Install? | Kelebihan                     |
|----------------|--------------|----------------|-------------------------------|
| html.parser    | HTML         | Tidak          | Ringan, bawaan Python         |
| lxml           | HTML & XML   | Ya             | Cepat dan fleksibel           |
| html5lib       | HTML5        | Ya             | Paling akurat, seperti browser|
| lxml-xml       | XML          | Ya             | Terbaik untuk XML             |
|----------------|--------------|----------------|-------------------------------|

---

## 🔹 1. Menggunakan html.parser (Built-in Python)

### 📌 Kode:
```python
from bs4 import BeautifulSoup

html = "<html><head><title>Test</title></head><body><h1>Welcome</h1></body></html>"
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
```

### ✅ Output:
```html
<html>
 <head>
  <title>
   Test
  </title>
 </head>
 <body>
  <h1>
   Welcome
  </h1>
 </body>
</html>
```

### ✔️ Kelebihan:
- Tidak perlu instalasi
- Ringan dan cukup untuk HTML sederhana

### ❌ Kekurangan:
- Kurang tangguh untuk HTML yang rusak

---

## 🔹 2. Menggunakan lxml

### 📦 Instalasi:
```bash
pip install lxml
```

### 📌 Kode:
```python
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
```

### ✅ Output: Sama seperti html.parser

### ✔️ Kelebihan:
- Cepat
- Bisa menangani HTML rusak

### ❌ Kekurangan:
- Harus install `lxml`

---

## 🔹 3. Menggunakan html5lib

### 📦 Instalasi:
```bash
pip install html5lib
```

### 📌 Kode:
```python
soup = BeautifulSoup(html, 'html5lib')
print(soup.prettify())
```

### ✅ Output: Sama, tapi bisa lebih "rapi" dan seperti browser

### ✔️ Kelebihan:
- Parsing paling akurat
- Meniru cara browser bekerja

### ❌ Kekurangan:
- Paling lambat
- Harus install html5lib

---

## 🔹 4. Menggunakan lxml-xml (Khusus XML)

### 📌 Kode:
```python
xml = "<data><item>Item 1</item><item>Item 2</item></data>"
soup = BeautifulSoup(xml, 'lxml-xml')
print(soup.prettify())
```

### ✅ Output:
```xml
<data>
 <item>
  Item 1
 </item>
 <item>
  Item 2
 </item>
</data>
```

### ✔️ Kelebihan:
- Ideal untuk XML
- Menjaga struktur XML dan namespace

---

## 📌 Perbandingan Kinerja

|------------|---------------|----------------|-------------------|
| Parser     |   Kecepatan   |    Akurasi    |  Bisa HTML Rusak?  |
|------------|---------------|----------------|-------------------|
| html.parser| ⭐⭐⭐⭐    | ⭐⭐          | ❌                |
| lxml       | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐    | ✅                |
| html5lib   | ⭐⭐         | ⭐⭐⭐⭐⭐  | ✅✅              |
| lxml-xml   | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐    | ❌ (khusus XML)   |
|------------|---------------|----------------|-------------------|

---

## 📘 Kesimpulan

|----------------------------------------|---------------------|
| Gunakan Jika...                        | Rekomendasi Parser  |
|----------------------------------------|---------------------|
| Ingin cepat dan sederhana              | `html.parser`       |
| Butuh kecepatan + fleksibilitas        | `lxml`              |
| Butuh hasil persis seperti browser     | `html5lib`          |
| Parsing file XML                       | `lxml-xml`          |
|----------------------------------------|---------------------|

---