from PIL import Image
import pytesseract
from openpyxl import load_workbook

im = Image.open("test1.jpg")

text = pytesseract.image_to_string(im, lang='eng')

print(text)


