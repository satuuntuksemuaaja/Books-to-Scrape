import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL halaman utama situs
url = "https://books.toscrape.com/"

# Kirim permintaan ke halaman utama
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Variabel untuk menyimpan data buku
books_data = []

# Ambil data setiap buku pada halaman utama
book_list = soup.find_all('article', class_='product_pod')
for book in book_list:
    # Ambil judul
    title = book.h3.a['title']
    
    # Ambil harga
    price = book.find('p', class_='price_color').get_text(strip=True)
    
    # Ambil rating
    rating = book.p['class'][1]  # Rating berada di kelas kedua, misalnya "star-rating Three"
    
    # Tambahkan data buku ke list
    books_data.append({
        'Title': title,
        'Price': price,
        'Rating': rating
    })

# Buat DataFrame dari data buku
df = pd.DataFrame(books_data)

# Tampilkan tabel
print(df)
