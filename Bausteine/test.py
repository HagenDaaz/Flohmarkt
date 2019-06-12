from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook

liste=[1,4,3]
Spalte="A"

wb = load_workbook(filename = 'test.xlsx')

dest_filename = 'test.xlsx'

ws1 = wb.active
ws1.title = "WebData"

#for i in liste:
ws1('A1')=5

wb.save(filename = dest_filename)