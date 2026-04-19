import os
import re
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fix_paths_in_file(filepath):
    rel_path = os.path.relpath(filepath, BASE_DIR)
    depth = rel_path.count(os.sep)
    prefix = "../" * depth if depth > 0 else ""

    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    modified = False

    # link etiketleri (CSS)
    for tag in soup.find_all("link", href=True):
        href = tag["href"]
        if not href.startswith(("http", "https", "//", "data:", "#")):
            clean = re.sub(r'^(\.\./)*', '', href)
            new_href = prefix + clean
            if tag["href"] != new_href:
                tag["href"] = new_href
                modified = True

    # script etiketleri (JS)
    for tag in soup.find_all("script", src=True):
        src = tag["src"]
        if not src.startswith(("http", "https", "//", "data:", "#")):
            clean = re.sub(r'^(\.\./)*', '', src)
            new_src = prefix + clean
            if tag["src"] != new_src:
                tag["src"] = new_src
                modified = True

    # img etiketleri
    for tag in soup.find_all("img", src=True):
        src = tag["src"]
        if not src.startswith(("http", "https", "//", "data:", "#")):
            clean = re.sub(r'^(\.\./)*', '', src)
            new_src = prefix + clean
            if tag["src"] != new_src:
                tag["src"] = new_src
                modified = True

    # css background-image url() düzeltmeleri (inline style veya style etiketi içinde)
    for tag in soup.find_all(style=True):
        style = tag["style"]
        # arka plan resmi varsa
        if "url(" in style:
            # basit bir düzeltme (gelişmiş regex yapılabilir ama şimdilik temel)
            pass  # bu kısmı atlayalım, gerekirse sonra ekleriz

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True
    return False

print("CSS/JS yolları düzeltiliyor...\n")
count = 0
for root, dirs, files in os.walk(BASE_DIR):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.htm')):
            filepath = os.path.join(root, file)
            if fix_paths_in_file(filepath):
                count += 1
                print(f"✓ {os.path.relpath(filepath, BASE_DIR)}")

print(f"\n✅ {count} dosya güncellendi.")