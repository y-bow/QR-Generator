# QR Code Generator (Python)

This is a simple QR Code generator built using Python.

I made this project to create permanent QR codes without depending on online websites.  
The URL is directly encoded into the image, so the QR will not expire.

---

## Features

- Generates permanent QR codes  
- Automatically creates a folder for output  
- Generates 5 QR code variants:
  - Black on White  
  - White on Black  
  - Black on Transparent  
  - White on Transparent  
  - Custom Color Variant  
- Supports user-defined QR and background colors  
- Transparent background support  

---

## Tech Used

- Python  
- qrcode library  
- Pillow (PIL)  
- os module  

---

## Installation

Install the required libraries:

```bash
pip install qrcode[pil] pillow
```

---

## How to Run

```bash
python main.py
```

The program will:

1. Ask for a URL  
2. Ask for a folder name  
3. Ask for custom colors  
4. Generate all QR images inside the created folder  

---


## Future Improvements

- Add logo in center  
- High resolution export  
- Batch QR generation  
- GUI version  
