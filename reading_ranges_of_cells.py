import openpyxl

wb = openpyxl.Workbook()

ws1 = wb.create_sheet("sheet_1")



ws1["A1"] = "A1"
ws1["A2"] = "A2"
ws1["B1"] = "B1"
ws1["B2"] = "B2"
ws1["C1"] = "C1"
ws1["C2"] = "C2"


cell_range = ws1["A1":"C2"]

print(cell_range)
wb.save("ranges_cells.xlsx")