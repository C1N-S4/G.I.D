import os
import requests
from bs4 import BeautifulSoup

hedef_kelime = input("Lütfen hedef kelimeyi girin: ")

url = f"https://www.google.com.tr/search?q={hedef_kelime}&tbm=isch"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
img_tags = soup.find_all("img")
img_urls = [img["data-src"] for img in img_tags if "data-src" in img.attrs]

kayit_yolu = os.path.join(os.path.expanduser("~"), "Desktop", hedef_kelime)
os.makedirs(kayit_yolu, exist_ok=True)

for i, url in enumerate(img_urls):
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        dosya_adi = f"{hedef_kelime}_{i+1}.jpg"
        dosya_yolu = os.path.join(kayit_yolu, dosya_adi)
        with open(dosya_yolu, "wb") as f:
            f.write(res.content)
    except Exception as e:
        print(f"Hata oluştu: {e}")

print("Tamamlandı!")
