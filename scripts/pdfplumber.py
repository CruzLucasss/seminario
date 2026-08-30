# !pip install pdfplumber
# !pip install urllib3 

import requests
import pdfplumber
import urllib3
import os

# Silenciar las advertencias SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL_PDF = "https://bo.unsa.edu.ar/cdfro/R2026/Res.CD-ORAN-269-2026.pdf"
ARCHIVO_TEMP = "temp_plumber.pdf"
ARCHIVO_TXT = "Res.CD-ORAN-269-2026_plumber.txt"

print("1. Descargando resolución con tablas...")
res = requests.get(URL_PDF, verify=False)

if res.status_code == 200:
    with open(ARCHIVO_TEMP, "wb") as f:
        f.write(res.content)
    
    print("2. Procesando estructura y tablas con pdfplumber...")
    texto_completo = ""
    
    # Abrir el PDF con pdfplumber
    with pdfplumber.open(ARCHIVO_TEMP) as pdf:
        for i, pagina in enumerate(pdf.pages):
            # layout=True es la clave: respeta los espacios en blanco de las tablas
            # para que el texto plano refleje visualmente las columnas
            texto_pagina = pagina.extract_text(layout=True)
            
            if texto_pagina:
                texto_completo += texto_pagina + "\n\n--- FIN DE PÁGINA ---\n\n"

    # Limpiar el archivo temporal
    if os.path.exists(ARCHIVO_TEMP):
        os.remove(ARCHIVO_TEMP)

    print("3. Guardando resultados...")
    with open(ARCHIVO_TXT, "w", encoding="utf-8") as f:
        f.write(texto_completo)
        
    print(f"¡Éxito! Puedes abrir '{ARCHIVO_TXT}' para comparar cómo se extrajeron las tablas.")

else:
    print(f"Error al intentar descargar el archivo. Código HTTP: {res.status_code}")