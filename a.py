import os
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Sabit ön ek
PREFIX = "GÜVEN Su Arıtma Sistemleri | Gaziantep Su Arıtma Servisi"

# Dosya adına göre özel sonekler (istersen buraya ekleme yapabilirsin)
OZEL_SONEKLER = {
    "index.html": "",  # ana sayfada sonek olmasın
    "hakkimizda.html": "Hakkımızda",
    "hizmetlerimiz.html": "Hizmetlerimiz",
    "iletisim.html": "İletişim",
    "urunlerimiz.html": "Ürünlerimiz",
    "blog.html": "Blog",
    "ekibimiz.html": "Ekibimiz",
    "foto-galeri.html": "Foto Galeri",
    "video-galeri.html": "Video Galeri",
    "sikca-sorulanlar.html": "Sıkça Sorulanlar",
    "talep.html": "Servis Talep Formu",
}

def get_title(filename):
    """Dosya adına göre başlık oluştur"""
    if filename in OZEL_SONEKLER:
        sonek = OZEL_SONEKLER[filename]
    else:
        # Eğer özel tanımlı değilse, dosya adından üret (uzantısız, tireleri boşluk yap, baş harfleri büyüt)
        name = os.path.splitext(filename)[0]
        sonek = name.replace("-", " ").title()
    
    if sonek:
        return f"{PREFIX} - {sonek}"
    else:
        return PREFIX

def update_title(filepath):
    filename = os.path.basename(filepath)
    new_title = get_title(filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    modified = False
    
    if soup.title:
        if soup.title.string != new_title:
            soup.title.string = new_title
            modified = True
    else:
        title_tag = soup.new_tag("title")
        title_tag.string = new_title
        if soup.head:
            soup.head.append(title_tag)
        modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True
    return False

def main():
    print("Her sayfaya özel başlıklar oluşturuluyor...\n")
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith(('.html', '.htm')):
                filepath = os.path.join(root, file)
                if update_title(filepath):
                    count += 1
                    rel = os.path.relpath(filepath, BASE_DIR)
                    print(f"✓ Güncellendi: {rel} -> {get_title(file)}")
    
    print(f"\n✅ Toplam {count} dosya güncellendi.")
    print("\nŞimdi sırasıyla şu komutları çalıştır:")
    print("  git add .")
    print('  git commit -m "Her sayfaya ozel basliklar eklendi"')
    print("  git push")

if __name__ == "__main__":
    main()