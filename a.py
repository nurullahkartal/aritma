import os

def her_seyi_onarma():
    html_dosyalari = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Tüm ihtimallere karşı (Themify, FA4, FA6) çalışan sağlam CDN linkleri
    ikon_paketleri = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lykmapipo/themify-icons@0.1.2/css/themify-icons.css">
    """
    
    print("🚀 Geniş kapsamlı ikon onarımı başlatıldı...")

    for dosya in html_dosyalari:
        with open(dosya, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()

        # 1. Eski, bozuk ikon linklerini temizle (Tekrar etmemesi için)
        import re
        icerik = re.sub(r'<link.*?href=".*?themify.*?".*?>', '', icerik)
        icerik = re.sub(r'<link.*?href=".*?flaticon.*?".*?>', '', icerik)

        # 2. Yeni paketleri </head> öncesine ekle
        if '</head>' in icerik:
            # Eğer daha önce eklediğimiz kod varsa onu da yenisiyle değiştirelim
            if 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css' in icerik:
                icerik = icerik.replace('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">', ikon_paketleri)
            else:
                icerik = icerik.replace('</head>', ikon_paketleri + '\n</head>')
        
        with open(dosya, 'w', encoding='utf-8') as f:
            f.write(icerik)
        print(f"✅ {dosya} dosyasının menü okları ve ikonları tazelendi.")

    print("\n🏁 Operasyon bitti haci! Şimdi o oklar mecburen gelecek.")

if __name__ == "__main__":
    her_seyi_onarma()