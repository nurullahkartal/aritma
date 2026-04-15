import os

def klasor_yollarini_tekellestir():
    html_dosyalari = [f for f in os.listdir('.') if f.endswith('.html')]
    
    print("🚀 'assets' yolları 'aritma_files' olarak güncelleniyor...")

    for dosya in html_dosyalari:
        with open(dosya, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()

        # 1. href="assets/ -> href="aritma_files/
        icerik = icerik.replace('href="assets/', 'href="aritma_files/')
        
        # 2. src="assets/ -> src="aritma_files/
        icerik = icerik.replace('src="assets/', 'src="aritma_files/')
        
        # 3. Eğer tırnaksız veya farklı kombinasyonlar varsa onları da kapsayalım
        icerik = icerik.replace('="assets/', '="aritma_files/')

        with open(dosya, 'w', encoding='utf-8') as f:
            f.write(icerik)
        print(f"✅ {dosya} yolu güncellendi.")

    print("\n🏁 Operasyon bitti haci! Artık site sadece 'aritma_files' klasörüne bakıyor.")

if __name__ == "__main__":
    klasor_yollarini_tekellestir()