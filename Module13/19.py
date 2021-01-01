
price = 0
discount_pers = 10

ticket_quantity = input("Укажите количество билетов:")

for i in range(int(ticket_quantity)):
    age = input("Укажите возраст:")
    if int(age) < 18:
        price += 0
    elif 18 <= int(age) < 25:
        price += 990
    elif int(age) >= 25:
        price += 1390

if int(ticket_quantity) > 3:
    price = price - price * discount_pers / 100

print(price)
