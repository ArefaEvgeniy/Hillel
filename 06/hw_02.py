# Ваше завдання — написати програму, яка переводить число у формат часу у
# читальному вигляді. Користувач повинен ввести число більше або дорівнює 0 і
# менше ніж 8640000. Число, яке є кількістю секунд, необхідно перевести в дні,
# години, хвилини та секунди. Ну і додатковим завданням є турбота про виведення.
#
# Слово "день" підбирається на основі кількості днів, а години, хвилини і
# секунди повинні заповнюватися нулями при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі
# 24 * 60 * 60 сек. Тобто використовуючи функцію divmod або методи поділу
# // і % вам необхідно знайти відповідну кількість днів, годин, хвилин, а те
# що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)
#
# Приклад:
# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

