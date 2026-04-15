import os

def pro_ikonlari_ucretsiz_yap():
    html_dosyalari = [f for f in os.listdir('.') if f.endswith('.html')]
    
    print("🚀 Pro ikonlar Free versiyona dönüştürülüyor...")

    for dosya in html_dosyalari:
        with open(dosya, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()

        # 1. fal (Light - Pro) olanları fas (Solid - Free) yap
        # 'fal ' şeklinde sonunda boşlukla aratıyoruz ki başka kelimelerle karışmasın
        icerik = icerik.replace('fal ', 'fas ')
        
        # 2. Eğer far (Regular) olup da görünmeyen varsa onları da fas yapabiliriz
        # icerik = icerik.replace('far ', 'fas ')

        with open(dosya, 'w', encoding='utf-8') as f:
            f.write(icerik)
        print(f"✅ {dosya} dosyasındaki Pro ikonlar halledildi.")

    print("\n🏁 İşlem bitti haci! Şimdi o oklar ve menü ikonları 'ücretsiz' ama sağlam görünecek.")

if __name__ == "__main__":
    pro_ikonlari_ucretsiz_yap()