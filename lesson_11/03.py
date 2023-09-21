# Використовуючи дані з минулого прикладу, спочатку записати їх у файл
# Excel-формату, а потім зчитати зі збереженого файлу

import openpyxl

name_of_fields = ["Ім'я", "Клас", "Вік"]
field_01 = ["Євген", "3", "10"]
field_02 = ["Сашко", "5", "12"]
field_03 = ["Михайло", "11", "18"]

woork_book = openpyxl.Workbook()
print(woork_book.sheetnames)

woork_book.create_sheet(title='Перший лист', index=0)
print(woork_book.sheetnames)

woork_book.remove(woork_book['Sheet'])
print(woork_book.sheetnames)

sheet = woork_book['Перший лист']
print(sheet)

for row_index, row in enumerate((name_of_fields, field_01, field_02, field_03)):
  for col_index, value in enumerate(row):  # ["Євген", "3", "10"]
    cell = sheet.cell(row=row_index + 1, column=col_index + 1)
    cell.value = value

woork_book.save('task_03.xlsx')


