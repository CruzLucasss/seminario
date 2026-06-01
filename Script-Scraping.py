#importaciones de librerias|| si lleva ! es porque en colab indica que se ejecuta desde la terminal
#!pip install PyMuPDF
#!pip install pypdf

import requests
import pymupdf
from deep_translator import GoogleTranslator

URL_PDF = "https://bo.unsa.edu.ar/dfro/R2026/Res.D-ORAN-088-2026.pdf"

# Descargar PDF
temp = "temp.pdf"
res = requests.get(URL_PDF, verify=False)
open(temp, "wb").write(res.content)

# Extraer texto
doc = pymupdf.open(temp)
texto = "".join(p.get_text() for p in doc)
doc.close()

# Traducir e imprimir por partes
translator = GoogleTranslator(source='auto', target='es')
paso = 4000

print("\n--- TEXTO TRADUCIDO ---\n")

for i in range(0, len(texto), paso):
    parte = texto[i:i+paso]
    traducido = translator.translate(parte)
    
    print(traducido)
    print("\n" + "-"*50 + "\n")  # separador visual entre bloques

print("\n--- FIN ---")
