orange_price = 17.5
my_money = 20
orange_good = False

if my_money > orange_price and orange_good is True:
    # Цей набір команд буде виконано лише в тому випадку,
    # коли my_money буде більшим, ніж orange_price
    my_money -= orange_price
    print("I buy orange")
    print(my_money)
print("The end")


# True and True = True      1 x 1 = 1
# True and False = False    1 x 0 = 0
# False and True = False    0 x 1 = 0
# False and False = False   0 x 0 = 0
