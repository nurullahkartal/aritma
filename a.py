import os
import re
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fix_paths_in_file(filepath):
    # Dosyanın ana dizine göre derinliğini hesapla (kaç klasör içeride)
    rel_path = os.path.relpath(filepath, BASE_DIR)
    depth = rel_path.count(os.sep)
    prefix = "../" * depth if depth > 0 else ""

    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    modified = False

    # 1. link etiketleri (CSS, favicon vb.)
    for tag in soup.find_all("link", href=True):
        href = tag["href"]
        if not href.startswith(("http", "https", "//", "data:", "#")):
            # Eğer zaten ../ ile başlıyorsa önce temizle
            clean_href = re.sub(r'^(\.\./)*', '', href)
            new_href = prefix + clean_href
            tag["href"] = new_href
            modified = True

    # 2. script etiketleri (JS)
    for tag in soup.find_all("script", src=True):
        src = tag["src"]
        if not src.startswith(("http", "https", "//", "data:", "#")):
            clean_src = re.sub(r'^(\.\./)*', '', src)
            new_src = prefix + clean_src
            tag["src"] = new_src
            modified = True

    # 3. img etiketleri
    for tag in soup.find_all("img", src=True):
        src = tag["src"]
        if not src.startswith(("http", "https", "//", "data:", "#")):
            clean_src = re.sub(r'^(\.\./)*', '', src)
            new_src = prefix + clean_src
            tag["src"] = new_src
            modified = True

    # 4. a etiketleri (href) - sadece göreceli yollar için
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        if not href.startswith(("http", "https", "//", "mailto:", "tel:", "#", "javascript:")):
            # .html uzantılı veya klasör adı olanlar
            if href.endswith(".html") or "/" in href:
                clean_href = re.sub(r'^(\.\./)*', '', href)
                new_href = prefix + clean_href
                tag["href"] = new_href
                modified = True

    # 5. form action (eğer göreceli ise)
    for tag in soup.find_all("form", action=True):
        action = tag["action"]
        if action and not action.startswith(("http", "https", "//", "#")):
            clean_action = re.sub(r'^(\.\./)*', '', action)
            new_action = prefix + clean_action
            tag["action"] = new_action
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True
    return False

def main():
    print("Tüm kaynak yolları düzeltiliyor...\n")
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        # .git klasörünü atla
        if '.git' in root:
            continue
        for file in files:
            if file.endswith(".html") or file.endswith(".htm"):
                filepath = os.path.join(root, file)
                if fix_paths_in_file(filepath):
                    count += 1
                    rel = os.path.relpath(filepath, BASE_DIR)
                    print(f"✓ Düzeltildi: {rel}")
    print(f"\n✅ Toplam {count} dosya güncellendi.")
    print("\nŞimdi sırasıyla şu komutları çalıştır:")
    print("  git add .")
    print('  git commit -m "Fix: CSS, JS ve resim yollari duzeltildi"')
    print("  git push")

if __name__ == "__main__":
    main()