import openpyxl


wb = openpyxl.load_workbook('task_03+.xlsx')
print(wb.sheetnames)

sheet = wb.active
print(sheet)

print(sheet['A1'].value)

rows = sheet.max_row
cols = sheet.max_column

data = []
for row in range(1, rows + 1):
  string = ''
  for col in range(1, cols + 1):
    cell = sheet.cell(row=row, column=col)
    string += str(cell.value) + ' '
  data.append(string.strip())

print(data)
