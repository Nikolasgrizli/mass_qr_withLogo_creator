import qrcode
from PIL import Image
import csv
import os

# === Налаштування ===
CSV_FILE = "src/qr_data.csv"        # ваш список з URL
LOGO_FILE = "src/fire.png"        # логотип
OUTPUT_DIR = "done/qr_codes"       # куди зберігати QR
FILL_COLOR = "#5F2F1C"        # колір QR (hex або назва, напр. "black")
BACK_COLOR = "#EBE4D5"          # фон QR
LOGO_SIZE = 120                # розмір логотипа в пікселях

# === Підготовка ===
os.makedirs(OUTPUT_DIR, exist_ok=True)
logo = Image.open(LOGO_FILE).convert("RGBA")

# Розміри оригінального зображення
w, h = logo.size  # logo.size повертає tuple (width, height)

# Обчислення нового розміру з збереженням пропорцій
if w > h:
    new_w = LOGO_SIZE
    new_h = int(h * (LOGO_SIZE / w))
else:
    new_h = LOGO_SIZE
    new_w = int(w * (LOGO_SIZE / h))

# Зміна розміру
logo = logo.resize((new_w, new_h), Image.LANCZOS)


# === Читання CSV ===
with open(CSV_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        label = row["label"]
        url = row["url"]

        # Генерація QR
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,border=0)
        qr.add_data(url)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR).convert("RGBA")

        # Вставка логотипу
        pos = ((img_qr.size[0] - new_w) // 2, (img_qr.size[1] - new_h) // 2)
        img_qr.paste(logo, pos, mask=logo)

        # Збереження
        output_path = os.path.join(OUTPUT_DIR, f"{label}.png")
        img_qr.save(output_path)

        print(f"[+] Збережено: {output_path}")

print("✅ Усі QR-коди згенеровані!")
