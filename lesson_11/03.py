# Используя данные из прошлого примера,
# сначала записать их в файл Excel-формата,
# а затем считать из сохранённого файла

import openpyxl


name_of_fields = ["Имя", "Класс", "Возраст"]
field_01 = ["Женя", "3", "10"]
field_02 = ["Саша", "5", "12"]
field_03 = ["Маша", "11", "18"]

wb = openpyxl.Workbook()
print(wb.sheetnames)

wb.create_sheet(title='Первый лист', index=0)
print(wb.sheetnames)

sheet = wb['Первый лист']
print(sheet)

for row_index, row in enumerate((name_of_fields, field_01, field_02, field_03)):
    for col_index, value in enumerate(row):
        cell = sheet.cell(row=row_index+1, column=col_index+1)
        cell.value = int(value) if value.isdigit() else value

wb.save('test.xlsx')


