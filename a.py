import os
import re
from bs4 import BeautifulSoup

# Site ana dizini (scriptin bulunduğu klasör)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Her sayfa için özel başlık ve açıklamalar
PAGE_META = {
    "index.html": {
        "title": "GÜVEN Su Arıtma Sistemleri | Gaziantep Su Arıtma Cihazı Servisi",
        "description": "Gaziantep'te profesyonel su arıtma cihazı satış, kurulum, filtre değişimi ve servis hizmeti. 12 yıllık tecrübe, uygun fiyat ve ücretsiz keşif."
    },
    "hakkimizda.html": {
        "title": "Hakkımızda | GÜVEN Su Arıtma Sistemleri Gaziantep",
        "description": "GÜVEN Su Arıtma, 2014'ten beri Gaziantep'te evsel ve endüstriyel su arıtma çözümleri sunar. Temiz su için güvenilir adresiniz."
    },
    "hizmetlerimiz.html": {
        "title": "Su Arıtma Hizmetlerimiz | GÜVEN Su Arıtma Gaziantep",
        "description": "Su arıtma cihazı satışı, kurulum, filtre değişimi, arıza onarım ve yedek parça hizmetleri. Gaziantep'in tüm ilçelerine 7/24 servis."
    },
    "iletisim.html": {
        "title": "İletişim | GÜVEN Su Arıtma Sistemleri Gaziantep",
        "description": "GÜVEN Su Arıtma iletişim bilgileri: Adres Şehitkamil/Gaziantep, Telefon 0 (541) 515 30 10. Servis talep formu için hemen tıklayın."
    },
    "urunlerimiz.html": {
        "title": "Su Arıtma Cihazları ve Fiyatları | GÜVEN Su Arıtma",
        "description": "Gaziantep'te satılık en iyi su arıtma cihazları. Tezgah altı, tezgah üstü, pompalı ve pompasız modeller. Uygun fiyat ve taksit imkanı."
    },
    "blog.html": {
        "title": "Blog | Su Arıtma Rehberi ve Haberler | GÜVEN Su Arıtma",
        "description": "Su arıtma cihazları hakkında bilgilendirici yazılar, bakım ipuçları ve sektör haberleri. Sağlıklı suya dair her şey."
    },
    "ekibimiz.html": {
        "title": "Ekibimiz | GÜVEN Su Arıtma Sistemleri",
        "description": "GÜVEN Su Arıtma'nın uzman teknisyen ve satış ekibi. Profesyonel ve sertifikalı personelimizle hizmetinizdeyiz."
    },
    "foto-galeri.html": {
        "title": "Foto Galeri | GÜVEN Su Arıtma Sistemleri",
        "description": "GÜVEN Su Arıtma'nın kurulum, servis ve ürün fotoğrafları. Çalışmalarımızı yakından görün."
    },
    "video-galeri.html": {
        "title": "Video Galeri | GÜVEN Su Arıtma",
        "description": "Su arıtma cihazı tanıtım ve kurulum videoları. GÜVEN Su Arıtma'nın YouTube kanalından örnekler."
    },
    "sikca-sorulanlar.html": {
        "title": "Sıkça Sorulanlar | GÜVEN Su Arıtma Gaziantep",
        "description": "Su arıtma cihazları hakkında merak edilenler. Filtre değişimi, kurulum, fiyatlar ve bakım hakkında SSS."
    },
    "talep.html": {
        "title": "Servis Talep Formu | GÜVEN Su Arıtma",
        "description": "Su arıtma cihazınız için servis randevusu oluşturun. Arıza, bakım veya filtre değişimi için formu doldurun."
    }
}

# Schema.org JSON-LD (LocalBusiness)
SCHEMA_SCRIPT = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "GÜVEN Su Arıtma Sistemleri",
  "image": "https://aritma.nurullahkartal.com.tr/panel/uploads/settings_v/1280x720/guvensuaritma.png",
  "@id": "https://aritma.nurullahkartal.com.tr",
  "url": "https://aritma.nurullahkartal.com.tr",
  "telephone": "+905415153010",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "79065 Nolu Sok., No:43B",
    "addressLocality": "Şehitkamil",
    "addressRegion": "Gaziantep",
    "postalCode": "27000",
    "addressCountry": "TR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 37.203126,
    "longitude": 37.3399768
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday"
    ],
    "opens": "08:30",
    "closes": "18:30"
  },
  "sameAs": [
    "https://www.facebook.com/guvensu.aritma",
    "https://www.instagram.com/guvensuaritma/"
  ],
  "priceRange": "₺₺"
}
</script>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    filename = os.path.basename(filepath)
    modified = False

    # 1. Title güncelle
    if filename in PAGE_META:
        new_title = PAGE_META[filename]["title"]
        if soup.title:
            soup.title.string = new_title
        else:
            title_tag = soup.new_tag("title")
            title_tag.string = new_title
            if soup.head:
                soup.head.append(title_tag)
        modified = True

    # 2. Meta description güncelle
    if filename in PAGE_META:
        new_desc = PAGE_META[filename]["description"]
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc:
            meta_desc["content"] = new_desc
        else:
            meta = soup.new_tag("meta", attrs={"name": "description", "content": new_desc})
            if soup.head:
                soup.head.append(meta)
        modified = True

    # 3. Görsellere alt etiketi ekle (eksik olanlara)
    for img in soup.find_all("img"):
        if not img.get("alt"):
            # Dosya adından veya src'den anlamlı bir alt oluştur
            src = img.get("src", "")
            alt_text = "GÜVEN Su Arıtma Sistemleri"
            if "logo" in src.lower() or "guvensuaritma" in src.lower():
                alt_text = "GÜVEN Su Arıtma Sistemleri Gaziantep Logosu"
            elif "hizmet" in src.lower():
                alt_text = "Su Arıtma Cihazı Hizmeti"
            elif "urun" in src.lower():
                alt_text = "Su Arıtma Cihazı"
            elif "su-aritma" in src.lower():
                alt_text = "Su Arıtma Cihazı Görseli"
            img["alt"] = alt_text
            modified = True

    # 4. Schema.org ekle (sadece index.html'e)
    if filename == "index.html":
        # Önce var mı kontrol et, yoksa ekle
        existing = soup.find("script", {"type": "application/ld+json"})
        if existing:
            existing.decompose()
        soup.head.append(BeautifulSoup(SCHEMA_SCRIPT, "html.parser"))
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"✓ {filename} güncellendi.")
    else:
        print(f"- {filename} değişiklik yok.")

def main():
    print("SEO Optimizasyonu başlatılıyor...\n")
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".html") or file.endswith(".htm"):
                filepath = os.path.join(root, file)
                process_file(filepath)
    print("\n✅ Tüm işlemler tamamlandı. Şimdi 'git add . && git commit -m \"SEO otomatik güncelleme\" && git push' yapabilirsiniz.")

if __name__ == "__main__":
    main()