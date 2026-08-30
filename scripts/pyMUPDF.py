# !pip install PyMuPDF
# !pip install urllib3 

import requests
import pymupdf
import urllib3
import os

# Silenciar las advertencias de seguridad por usar verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL_PDF = "https://bo.unsa.edu.ar/cdfro/R2026/Res.CD-ORAN-269-2026.pdf"
ARCHIVO_TEMP = "temp.pdf"
ARCHIVO_TXT = "Res.D-ORAN-088-2026.txt"

print("1. Descargando resolución...")
res = requests.get(URL_PDF, verify=False)

# Verificar que la descarga fue exitosa (código 200)
if res.status_code == 200:
    # Guardar el PDF temporalmente
    with open(ARCHIVO_TEMP, "wb") as f:
        f.write(res.content)
    
    print("2. Extrayendo texto del PDF...")
    doc = pymupdf.open(ARCHIVO_TEMP)
    texto_completo = "".join(page.get_text() for page in doc)
    doc.close()

    # Opcional: Eliminar el PDF temporal si ya no lo necesitas para ahorrar espacio
    if os.path.exists(ARCHIVO_TEMP):
        os.remove(ARCHIVO_TEMP)

    print("3. Guardando en archivo .txt...")
    # Guardar el texto extraído en formato txt (usando utf-8 para los acentos y eñes)
    with open(ARCHIVO_TXT, "w", encoding="utf-8") as f:
        f.write(texto_completo)
        
    print(f"¡Éxito! El documento está listo para el dataset en: {ARCHIVO_TXT}")

else:
    print(f"Error al intentar descargar el archivo. Código HTTP: {res.status_code}")