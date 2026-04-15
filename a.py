import os
import re

def her_seyi_benim_siteye_bagla():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Senin yeni ana yolun
    yeni_yol = "https://aritma.nurullahkartal.com.tr/aritma_files"
    
    # Eski sitenin genel URL yapısı (regex için)
    # Bu desen, eski sitenin linkini bulur ve sadece sonundaki dosya adını yakalar
    eski_url_deseni = r'https?://(?:www\.)?goldwatergaziantep\.com\.tr/[^"\')\s]*/([^"\')\s]+\.[a-zA-Z0-9]+)'
    
    print("🚀 Tüm dış linkler senin siteye ve aritma_files klasörüne taşınıyor...")

    for dosya in html_files:
        with open(dosya, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()
        
        # Fonksiyon: Yakalanan dosya adını senin yeni yolunla birleştirir
        def degistir(match):
            dosya_adi = match.group(1)
            return f"{yeni_yol}/{dosya_adi}"
        
        # Tüm eşleşmeleri değiştir (srcset, background-image, src fark etmez)
        yeni_icerik = re.sub(eski_url_deseni, degistir, icerik)
        
        with open(dosya, 'w', encoding='utf-8') as f:
            f.write(yeni_icerik)
        print(f"✅ {dosya} entegrasyonu tamamlandı.")

    print("\n🏁 Operasyon bitti haci! Artık site tamamen sana ve senin sunucuna bağlı.")

if __name__ == "__main__":
    her_seyi_benim_siteye_bagla()