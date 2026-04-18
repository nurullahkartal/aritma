import os
import shutil
from bs4 import BeautifulSoup

# Ana dizin (scriptin bulunduğu klasör)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# İşlem yapılmayacak dosyalar
EXCLUDE_FILES = {"index.html", "404.html", "tesekkurler.html", "robots.txt", "sitemap.xml"}

# Ana dizindeki tüm .html dosyalarını bul
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html") and f not in EXCLUDE_FILES]

print(f"Bulunan HTML dosyaları: {len(html_files)}")

# 1. Her dosya için klasör oluştur ve taşı
moved_files = {}
for html_file in html_files:
    # Klasör adı (uzantısız)
    folder_name = html_file.replace(".html", "")
    folder_path = os.path.join(BASE_DIR, folder_name)
    
    # Klasörü oluştur (varsa hata verme)
    os.makedirs(folder_path, exist_ok=True)
    
    # Dosyayı index.html olarak klasöre taşı
    old_path = os.path.join(BASE_DIR, html_file)
    new_path = os.path.join(folder_path, "index.html")
    shutil.move(old_path, new_path)
    
    moved_files[html_file] = folder_name
    print(f"✓ {html_file} → {folder_name}/index.html")

# 2. Tüm HTML dosyalarındaki bağlantıları güncelle
def update_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    modified = False
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        
        # Eğer href, taşınan dosyalardan birine işaret ediyorsa
        if href in moved_files:
            # href'i klasör adıyla değiştir (sonuna slash ekleyerek)
            new_href = moved_files[href] + "/"
            a_tag["href"] = new_href
            modified = True
        # Eğer href .html ile bitiyor ve dosya taşınmışsa (alt dizinlerdeki dosyalar için)
        elif href.endswith(".html") and os.path.basename(href) in moved_files:
            folder = moved_files[os.path.basename(href)]
            # Yolu güncelle (göreceli yolu koru)
            if href.startswith("../"):
                new_href = href.replace(os.path.basename(href), folder + "/")
            else:
                new_href = folder + "/"
            a_tag["href"] = new_href
            modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True
    return False

print("\nBağlantılar güncelleniyor...")
updated_count = 0
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".html") or file.endswith(".htm"):
            filepath = os.path.join(root, file)
            if update_links(filepath):
                updated_count += 1
                print(f"✓ Bağlantılar güncellendi: {os.path.relpath(filepath, BASE_DIR)}")

print(f"\n✅ İşlem tamamlandı! {len(html_files)} dosya taşındı, {updated_count} dosyada bağlantı güncellendi.")
print("\n📌 Not: Ana sayfanız (index.html) olduğu yerde kaldı.")
print("Şimdi aşağıdaki komutları çalıştırarak değişiklikleri GitHub'a gönderin:")
print("  git add .")
print('  git commit -m "Clean URLs: .html uzantıları kaldırıldı"')
print("  git push")