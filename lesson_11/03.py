# Використовуючи дані з минулого прикладу,
# спочатку записати їх у файл Excel-формату,
# а потім рахувати зі збереженого файлу


import openpyxl

name_of_fields = ["Ім'я", "Клас", "Вік"]
field_01 = ["Євген", "3", "10"]
field_02 = ["Сашко", "5", "12"]
field_03 = ["Михайло", "11", "18"]


wb = openpyxl.Workbook()
print(wb.sheetnames)

wb.create_sheet(title='Перший лист', index=0)
print(wb.sheetnames)

# wb.remove(wb['Перший лист'])
# print(wb.sheetnames)

sheet = wb['Перший лист']
print(sheet)

for row_index, row in enumerate((name_of_fields, field_01, field_02, field_03)):
    for col_index, value in enumerate(row):
        cell = sheet.cell(row=row_index+1, column=col_index+1)
        cell.value = value

wb.save('task_03.xlsx')


wb_2 = openpyxl.load_workbook('task_04.xlsx')
print(wb_2.sheetnames)

sheet_2 = wb_2.active
print(sheet_2)

print(sheet_2['C4'].value)
print(sheet_2['C5'].value)
print(sheet_2['C6'].value)

rows = sheet_2.max_row
cols = sheet_2.max_column
print(rows)
print(cols)

fields_value = []
for i in range(1, rows + 1):
    row_value = []
    for y in range(1, cols + 1):
        row_value.append(sheet_2.cell(row=i, column=y).value)
    fields_value.append(row_value)

print(fields_value)
