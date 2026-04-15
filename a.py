import os

def adresleri_sadelestir():
    # Aranacak ve değiştirilecek adresler
    eski_adres = "www.aritma.nurullahkartal.com.tr"
    yeni_adres = "aritma.nurullahkartal.com.tr"
    
    print(f"'{eski_adres}' -> '{yeni_adres}' dönüşümü başlatılıyor...\n")
    degistirilen_dosya_sayisi = 0

    # os.walk ile tüm alt klasörleri ve dosyaları tara
    for kok_dizin, alt_dizinler, dosyalar in os.walk('.'):
        for dosya in dosyalar:
            # Sadece metin tabanlı dosyaları kontrol et
            if dosya.endswith(('.html', '.css', '.js', '.json', '.txt')):
                dosya_yolu = os.path.join(kok_dizin, dosya)
                
                try:
                    with open(dosya_yolu, 'r', encoding='utf-8', errors='ignore') as f:
                        icerik = f.read()
                    
                    if eski_adres in icerik:
                        yeni_icerik = icerik.replace(eski_adres, yeni_adres)
                        
                        with open(dosya_yolu, 'w', encoding='utf-8') as f:
                            f.write(yeni_icerik)
                        
                        print(f"✅ Güncellendi: {dosya_yolu}")
                        degistirilen_dosya_sayisi += 1
                except Exception as e:
                    print(f"❌ Hata (Atlandı): {dosya_yolu} - {e}")

    print(f"\nİşlem bitti! Toplam {degistirilen_dosya_sayisi} dosya pırıl pırıl yapıldı.")

if __name__ == "__main__":
    adresleri_sadelestir()