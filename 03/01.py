orange_price = 17.5
my_money = 20

if my_money > orange_price:
    # Цей набір команд буде виконано лише в тому випадку,
    # коли my_money буде більшим, ніж orange_price
    my_money -= orange_price
    print("I buy orange")
    print(my_money)
else:
    print("У вас не достатньо коштів")
print("The end")
