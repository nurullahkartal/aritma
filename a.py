import os

def temizlik_yap():
    html_dosyalari = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # SENİN BİLGİLERİN - BURAYI DÜZELTEBİLİRSİN
    yeni_mail = "info@guvensuaritma.com" # Buraya kendi mailini yaz haci
    
    for dosya in html_dosyalari:
        with open(dosya, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()

        # 1. Eski mail adreslerini temizle
        icerik = icerik.replace("info@goldwatergaziantep.com.tr", yeni_mail)

        # 2. srcset içindeki dış bağlantılı logoları temizle (Sadece yerel logonu kullansın)
        import re
        icerik = re.sub(r'srcset="https://goldwatergaziantep.com.tr.*?"', '', icerik)

        # 3. Dışarıdan çekilen arka plan resimlerini yerelleştir (veya o linkleri temizle)
        # Şimdilik en azından senin klasöründeki resimlere yönlendirelim
        icerik = icerik.replace("https://goldwatergaziantep.com.tr/panel/uploads/slides_v/1920x650/su-aritma-cihazi-fiyatlari.jpg", "aritma_files/1.jpg")

        with open(dosya, 'w', encoding='utf-8') as f:
            f.write(icerik)
        print(f"✅ {dosya} temizlendi.")

if __name__ == "__main__":
    temizlik_yap()