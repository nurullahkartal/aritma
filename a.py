import os

def ikonlari_duzelt():
    html_dosyalari = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Çalışan en güncel ikon kütüphanesi linki
    yeni_ikon_linki = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    
    print("🛠️ İkon onarım operasyonu başladı...")

    for dosya in html_dosyalari:
        with open(dosya, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()

        # 1. Eski (bozuk olan) fontawesome linklerini temizle
        import re
        # aritma_files içindeki fontawesome.css linkini bulur ve siler
        icerik = re.sub(r'<link.*?href=".*?fontawesome.*?".*?>', '', icerik)

        # 2. Yeni ve çalışan linki </head> etiketinden hemen önce ekle
        if '</head>' in icerik:
            icerik = icerik.replace('</head>', yeni_ikon_linki + '\n</head>')
        
        with open(dosya, 'w', encoding='utf-8') as f:
            f.write(icerik)
        print(f"✅ {dosya} dosyasında ikonlar canlandırıldı.")

    print("\n🏁 İşlem bitti haci! Şimdi ikonlar fıstık gibi görünecek.")

if __name__ == "__main__":
    ikonlari_duzelt()