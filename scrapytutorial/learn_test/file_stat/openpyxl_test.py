# -*- coding: utf-8 -*-

import openpyxl
import warnings

file_path = 'C:\Users\Bain\Desktop\\1.xlsx'
warnings.simplefilter("ignore")
wb = openpyxl.load_workbook(file_path)
warnings.simplefilter("default")

sheet = wb.active
for cellObj in sheet.columns[1]:
    print(cellObj.value)
