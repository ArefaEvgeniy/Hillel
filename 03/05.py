orange_price = 17.5
my_money = 10
want_orange = False

if my_money > orange_price or want_orange is True:
    # Цей набір команд буде виконано лише в тому випадку,
    # коли my_money буде більшим, ніж orange_price
    my_money -= orange_price
    print("I buy orange")
    print(my_money)
print("The end")


# True or True = True      1 + 1 = 1
# True or False = True     1 + 0 = 1
# False or True = True     0 + 1 = 1
# False or False = False   0 + 0 = 0
