# QR Code Generator with Logo

**Description:**
A simple Python script that can generate a large number of QR codes with a logo inside and additional parameters.

---

## Features

* Generate multiple QR codes from a CSV file.
* Insert a custom logo in the center of each QR code.
* Maintain the logo's original proportions.
* Customize QR code color and background.
* Adjust QR code border size.

---

## Requirements

* Python 3.8+
* [Pillow](https://pypi.org/project/Pillow/)
* [qrcode](https://pypi.org/project/qrcode/)

Install dependencies:

```bash
pip install qrcode pillow
```

---

## Usage

1. Prepare a CSV file (`links.csv`) with columns `label` and `url`:

```csv
label,url
LABEL001,https://example.com/page1
LABEL002,https://example.com/page2
```

2. Place your logo as `logo.png` in the project directory.

3. Run the script:

```bash
python creator.py
```

4. The generated QR codes will appear in the `qr_codes/` folder.

---

## Notes

* Keep the logo simple for better QR code readability.
* Adjust `LOGO_SIZE` and `border` in the script to fit your needs.
* The script preserves the logo's aspect ratio automatically.
