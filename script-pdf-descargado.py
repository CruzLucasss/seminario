import pymupdf 
from pypdf import PdfReader
import os
import re

documento = pymupdf.open("C:/Carpeta_Lucas/seminario/resolucion-prueba.pdf")
for pagina in documento:
    print(pagina.get_text())

print("---------------------------------")    

documento = PdfReader("C:/Carpeta_Lucas/seminario/resolucion-prueba.pdf")
for pagina in documento.pages:
    print(pagina.extract_text())