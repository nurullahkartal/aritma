import os
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SWEETALERT_PATTERN = "npm/sweetalert2"
GMAPS_PATTERN = "maps.googleapis.com/maps/api/js"

count = 0
for root, dirs, files in os.walk(BASE_DIR):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.htm')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
            
            modified = False
            # SweetAlert2 scriptlerini sil
            for script in soup.find_all('script', src=True):
                if SWEETALERT_PATTERN in script['src']:
                    script.decompose()
                    modified = True
            
            # Google Maps API scriptlerini sil
            for script in soup.find_all('script', src=True):
                if GMAPS_PATTERN in script['src']:
                    script.decompose()
                    modified = True
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                count += 1
                print(f"✓ Temizlendi: {os.path.relpath(filepath, BASE_DIR)}")

print(f"\n✅ {count} dosya güncellendi.")