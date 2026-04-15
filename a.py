import os

def evrensel_ikon_enjektoru():
    html_dosyalari = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Dünyada kullanılan en yaygın 5 ikon kütüphanesi (CDN)
    evrensel_linkler = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lykmapipo/themify-icons@0.1.2/css/themify-icons.css">
    <link rel="stylesheet" href="https://cdn.lineicons.com/4.0/lineicons.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/icofont/1.0.1/css/icofont.min.css">
    """
    
    print("🚀 İkon kütüphaneleri çapraz ateşe alınıyor...")

    for dosya in html_dosyalari:
        with open(dosya, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()

        # 1. Daha önce eklediğimiz eski veya bozuk ikon linklerini temizle
        import re
        # Tüm olası ikon linklerini temizleyelim ki çakışmasın
        icerik = re.sub(r'<link.*?href=".*?fontawesome.*?".*?>', '', icerik)
        icerik = re.sub(r'<link.*?href=".*?themify.*?".*?>', '', icerik)
        icerik = re.sub(r'<link.*?href=".*?lineicons.*?".*?>', '', icerik)
        icerik = re.sub(r'<link.*?href=".*?icofont.*?".*?>', '', icerik)

        # 2. Evrensel paketi </head> etiketinden hemen önce yapıştır
        if '</head>' in icerik:
            icerik = icerik.replace('</head>', evrensel_linkler + '\n</head>')
        
        with open(dosya, 'w', encoding='utf-8') as f:
            f.write(icerik)
        print(f"✅ {dosya} için tüm ikon yolları döşendi.")

    print("\n🏁 Operasyon bitti haci! Şimdi o okların gelmeme ihtimali %1.")

if __name__ == "__main__":
    evrensel_ikon_enjektoru()