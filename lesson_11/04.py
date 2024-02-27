import openpyxl


wb = openpyxl.load_workbook('task_2.xlsx')
print(wb)
print(wb.sheetnames)

sheet = wb.active
print(sheet)

print(sheet['A4'].value)

rows = sheet.max_row
cols = sheet.max_column
print(rows)
print(cols)

data = []
for i in range(1, rows+1):
    field_data = []
    for j in range(1, cols+1):
        cell = sheet.cell(row=i, column=j)
        field_data.append(cell.value)
    data.append(field_data)

print(data)
