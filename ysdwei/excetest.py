import os
import time
from openpyxl import Workbook
excelPath = os.path.join(os.getcwd())
nameTime = time.strftime('%Y-%m-%d_%H-%M-%S')
excelName = 'Excel' + nameTime + '.xlsx'
ExcelFullName= os.path.join(excelPath,excelName)
wb = Workbook()
ws = wb.active
tableTitle = ['标题', '时间']
for col in range(len(tableTitle)):
    c = col + 1
    ws.cell(row=1, column=c).value = tableTitle[col]

for row in range(len(tableValues)):
    ws.append(tableValues[row])
    #wb.save(ExcelFullName)
    wb.save(filename=ExcelFullName)

print(excelPath)
print(nameTime)
print(ExcelFullName)