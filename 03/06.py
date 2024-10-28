orange_price = 17.5
my_money = 20
orange_good = False
not_green = False
green = False

if not (my_money > orange_price and (orange_good is True or not_green)):
    # Цей набір команд буде виконано лише в тому випадку,
    # коли my_money буде більшим, ніж orange_price
    my_money -= orange_price
    print("I buy orange")
    print(my_money)
print("The end")
