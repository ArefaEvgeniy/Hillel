import openpyxl


wb = openpyxl.load_workbook('test.xlsx')

sheets = wb.sheetnames
print(sheets)

sheet = wb.active
print(sheet)

print(sheet['A2'].value)

rows = sheet.max_row
columns = sheet.max_column

print(rows)
print(columns)
print('-' * 100)

new_values = []
for j in range(1, rows+1):
    values = []
    for i in range(1, columns+1):
        cell = sheet.cell(row=j, column=i)
        values.append(cell.value)
    new_values.append(values)
print(new_values)
