import openpyxl

wb = openpyxl.Workbook()
wb.save("first_wb.xlsx")

wb = openpyxl.load_workbook("test.xlsx")

for sheet in wb:
    print(sheet.title)