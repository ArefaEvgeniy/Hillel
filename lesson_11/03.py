# Используя данные из прошлого примера,
# сначала записать их в файл Excel-формата,
# а затем считать из сохранённого файла


import openpyxl

name_of_fields = ["Имя", "Класс", "Возраст"]
field_01 = ["Женя", "3", "10"]
field_02 = ["Саша", "5", "12"]
field_03 = ["Маша", "11", "18"]


work_book = openpyxl.Workbook()
print(work_book.sheetnames)

work_book.create_sheet('Первый лист', index=0)
print(work_book.sheetnames)

work_book.remove(work_book['Sheet'])
print(work_book.sheetnames)

sheet = work_book['Первый лист']
print(sheet)

sheet['A1'].value = 11
print(sheet['A1'].value)

sheet['B2'].value = sheet['A1'].value + 1
sheet['C3'].value = sheet['B2'].value + 1

work_book.save('task_03.xlsx')


work_book_2 = openpyxl.Workbook()
sheet = work_book_2['Sheet']

for row_index, row in enumerate((name_of_fields, field_01, field_02, field_03)):
    for col_index, value in enumerate(row):
        cell = sheet.cell(row=row_index+1, column=col_index+1)
        cell.value = value

work_book_2.save('task_04.xlsx')

print('-' * 50)

wb = openpyxl.load_workbook('task_05.xlsx')
print(wb.sheetnames)
sheet = wb.active
print(sheet)
print(sheet['A2'].value)

rows = sheet.max_row
cols = sheet.max_column
print(rows)
print(cols)

name_of_col = []
field_values = []
for row in range(1, rows+1):
    value = []
    for col in range(1, cols+1):
        cell = sheet.cell(row=row, column=col)
        if row == 1:
            name_of_col.append(cell.value)
        else:
            value.append(str(cell.value) if cell.value is not None else ' ')

    value = ', '.join(value)

    if row != 1:
        field_values.append(value)

print(name_of_col)
print(field_values)
