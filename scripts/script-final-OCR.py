import requests
import pytesseract
from pdf2image import convert_from_path
import urllib3
import os

# Silenciar advertencias de seguridad SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- RUTAS LOCALES EXACTAS ---
# Ruta por defecto donde se instala Tesseract en Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Ruta a tu carpeta bin de Poppler en el proyecto
RUTA_POPPLER = r'C:\Carpeta_Lucas\seminario\bin' 

# La resolución problemática llena de sellos y firmas
URL_PDF = "https://bo.unsa.edu.ar/cdfro/R2026/Res.CD-ORAN-201-2026.pdf"
ARCHIVO_TEMP = "temp_ocr.pdf"
ARCHIVO_TXT = "Res.CD-ORAN-201-2026_OCR.txt"

print("1. Descargando resolución...")
res = requests.get(URL_PDF, verify=False)

if res.status_code == 200:
    with open(ARCHIVO_TEMP, "wb") as f:
        f.write(res.content)
    
    print("2. Convirtiendo páginas del PDF a imágenes (Poppler)...")
    paginas = convert_from_path(ARCHIVO_TEMP, poppler_path=RUTA_POPPLER)
    
    texto_completo = ""
    
    print(f"3. Aplicando OCR a {len(paginas)} página(s) con Tesseract...")
    for i, pagina in enumerate(paginas):
        print(f"   Procesando página {i+1}...")
        # lang='spa' activa el diccionario en español
        texto_pagina = pytesseract.image_to_string(pagina, lang='spa')
        texto_completo += texto_pagina + "\n\n--- FIN DE PÁGINA ---\n\n"

    # Limpiamos el PDF temporal
    if os.path.exists(ARCHIVO_TEMP):
        os.remove(ARCHIVO_TEMP)

    print("4. Guardando el resultado limpio...")
    with open(ARCHIVO_TXT, "w", encoding="utf-8") as f:
        f.write(texto_completo)
        
    print(f"¡Proceso terminado! Revisa el archivo: {ARCHIVO_TXT}")

else:
    print(f"Error HTTP: {res.status_code}")