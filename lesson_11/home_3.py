# Прочитати збережений csv-файл із попереднього завдання та зберегти дані в
# excel-файл, Крім віку - стовпець з цими даними не потрібний.
# *Додаткове завдання не обов'язкове до виконання:
# розгорнути таблицю на дев'яносто градусів (стовпці стають рядками, а рядки
# стовпцями). До завдання прикріплений приклад як має виглядати змісту
# підсумкового файлу.

import openpyxl
import csv


with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    num_rows = sum(1 for row in csv_reader)

wb = openpyxl.Workbook()
ws = wb.active

for r, row in enumerate(rows, start=1):
    ws.cell(row=1, column=1, value='')
    ws.cell(row=1, column=r, value='Person ' + str(r - 1))
    for c, val in enumerate(row, start=2):
        if c == 4:
            continue
        ws.cell(row=c if c < 4 else c - 1, column=r, value=val)

wb.save('file_xlsx.xlsx')
wb.close()
