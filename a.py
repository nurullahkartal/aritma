import os

# === AYARLAR ===
html_dosya = "iletisim.html"

eski_klasor = "Gold Water Su Arıtma Sistemleri _ Gaziantep_files"
yeni_klasor = "aritma_files"

eski_link = "www.goldwatergaziantep.com.tr"
yeni_link = "www.aritma.nurullahkartal.com.tr"

eski_title = "Gold Water Su Arıtma Sistemleri | Gaziantep"
yeni_title = "Gaziantep Su Arıtma | GÜVEN Su Arıtma Sistemleri"

eski_logo = "goldwater-logo--1-.png"
yeni_logo = "guvensuaritma.png"


# === 1. KLASÖRÜ YENİDEN ADLANDIR ===
if os.path.exists(eski_klasor):
    os.rename(eski_klasor, yeni_klasor)
    print("✔ files klasörü değiştirildi")
else:
    print("⚠ files klasörü bulunamadı (zaten değişmiş olabilir)")


# === 2. HTML GÜNCELLE ===
if not os.path.exists(html_dosya):
    print("❌ HTML dosyası yok")
    exit()

with open(html_dosya, "r", encoding="utf-8") as f:
    icerik = f.read()

icerik = icerik.replace(eski_link, yeni_link)
icerik = icerik.replace(eski_title, yeni_title)
icerik = icerik.replace(eski_logo, yeni_logo)
icerik = icerik.replace(eski_klasor, yeni_klasor)

with open(html_dosya, "w", encoding="utf-8") as f:
    f.write(icerik)

print("🔥 hakkimda.html TAMAMEN GÜNCELLENDİ")