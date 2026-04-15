import os
import re

def link_uzantilarini_duzelt():
    html_dosyalari = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Düzeltilecek sayfaların listesi
    sayfalar = ['index', 'hakkimda', 'ekibimiz', 'iletisim', 'blog', 'sikca-sorulanlar']
    
    print("🔗 Sayfa linkleri kontrol ediliyor ve .html ekleniyor...")

    for dosya in html_dosyalari:
        with open(dosya, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()

        for sayfa in sayfalar:
            # Sadece tam eşleşen (sonunda .html olmayan) linkleri bul ve değiştir
            # Örn: href="index" -> href="index.html"
            eski_link = f'href="{sayfa}"'
            yeni_link = f'href="{sayfa}.html"'
            icerik = icerik.replace(eski_link, yeni_link)

        with open(dosya, 'w', encoding='utf-8') as f:
            f.write(icerik)
        print(f"✅ {dosya} dosyasındaki linkler bağlandı.")

    print("\n🏁 Operasyon bitti haci! Artık menü tıkır tıkır çalışacak.")

if __name__ == "__main__":
    link_uzantilarini_duzelt()