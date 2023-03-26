# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 12:57:33 2023

@author: R.R. Voordouw
"""

#Therod JPG2TXT
# Programma dat JPG files scant op tekst en deze tekst in een txt file plaatst.
# Zorg dat pytesseract geïnstalleerd is met: pip install pytesseract en in windows door het hier te downloaden: https://github.com/UB-Mannheim/tesseract/wiki
# https://github.com/UB-Mannheim/tesseract/wiki
# Importeren van functies

import pytesseract
from PIL import Image
from tkinter import filedialog, Tk
import os

# Maak een bestandsdialoog venster

root = Tk()
root.withdraw()

# Open het bestandsdialoogvenster om een JPG bestand te selecteren

file_path = filedialog.askopenfilename(filetypes=[("JPEG-bestanden", "*.jpg"), ("Alle bestanden", "*.*")])

# De bestandsnaam uit het JPG bestand halen
jpg_filename = os.path.basename(file_path)

# Extensie verwijderen uit de bestandsnaam

jpg_filename_no_ext = os.path.splitext(jpg_filename)[0]


# Afbeelding inlezen.
img = Image.open(file_path)

# Converteren van afbeelding'naar grijswaarden.

img = img.convert('L')

# Tekst uit de afbeelding halen
text = pytesseract.image_to_string(img)

# TXT file genereren
txt_filename = jpg_filename_no_ext + '.txt'

# Tekst opslaan in een TXT bestand.
with open(txt_filename, mode='w', encoding='utf-8') as file:
    file.write(text)
