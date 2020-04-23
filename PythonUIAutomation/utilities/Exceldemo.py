import openpyxl
openpyxl.load_workbook("/home/vandana/Downloads/Test-case-template-xls.xls")
sheet = book.active
sheet.cell(row=1,column = 2)
print(cell.value)
