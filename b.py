import os

klasor = "aritma_files"

if not os.path.exists(klasor):
    print("❌ klasör bulunamadı")
    exit()

degisen = 0

for root, dirs, files in os.walk(klasor):
    for file in files:
        if ".indir" in file:
            eski_path = os.path.join(root, file)

            yeni_isim = file.replace(".indir", "")
            yeni_path = os.path.join(root, yeni_isim)

            os.rename(eski_path, yeni_path)

            degisen += 1
            print(f"✔ değişti: {file} → {yeni_isim}")

print(f"🔥 TOPLAM DÜZENLENEN DOSYA: {degisen}")