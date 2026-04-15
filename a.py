import os
import re

# Yapılacak değişiklikler listesi
def siteyi_onar():
    # Klasördeki tüm html dosyalarını bul
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Yeni Footer (NKartal İmzası ve 2026 Copyright)
    yeni_footer = """
    <footer style="background: #f8f9fa; padding: 50px 0; text-align: center; border-top: 1px solid #eee; margin-top: 50px;">
        <div class="container">
            <img src="aritma_files/guvensuaritma.png" style="height: 30px; margin-bottom: 10px;" alt="Güven Su">
            <p style="font-size: 14px; color: #777;">&copy; 2026 | Tüm Hakları Saklıdır.</p>
            <hr style="width: 150px; margin: 20px auto; opacity: 0.1;">
            <p style="display: flex; align-items: center; justify-content: center; font-size: 18px; gap: 10px; color: #333;">
                Powered by 
                <a href="https://nurullahkartal.com.tr" target="_blank" style="text-decoration: none;">
                    <img src="aritma_files/nklogo.png" style="height: 80px !important;" alt="NKartal">
                </a>
            </p>
        </div>
    </footer>
    """

    for filename in html_files:
        print(f"--- {filename} Onarılıyor... ---")
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. .indir uzantılarını temizle
        content = content.replace('.js.indir', '.js')
        content = content.replace('.css.indir', '.css')
        content = content.replace('.png.indir', '.png')
        content = content.replace('.jpg.indir', '.jpg')
        content = content.replace('.jpeg.indir', '.jpeg')

        # 2. Eski Faviconu yerel yap (Eski linki bizim logoya yönlendir)
        content = re.sub(r'href="https://goldwatergaziantep.com.tr.*?"', 'href="aritma_files/guvensuaritma.png"', content)

        # 3. Ana Logoyu Güncelle (Eski logo yolunu bul ve bizimkiyle değiştir)
        # Mirror edilen sitelerde logo genelde goldwater-logo--1-.png ismindedir
        content = content.replace('goldwater-logo--1-.png', 'guvensuaritma.png')

        # 4. Footer Operasyonu
        # Mevcut footer etiketini bul ve bizim NKartal imzalı footer ile değiştir
        if '<footer' in content:
            content = re.sub(r'<footer.*?</footer>', yeni_footer, content, flags=re.DOTALL)
        else:
            # Eğer footer etiketi yoksa body kapanışından önce ekle
            content = content.replace('</body>', yeni_footer + '</body>')

        # 5. Kaydet
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("\n✅ Operasyon Tamam Hacı! Tüm dosyalar jilet gibi oldu.")

if __name__ == "__main__":
    siteyi_onar()