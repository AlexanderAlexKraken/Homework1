print("Доброго времени суток! Сегодня мы хотим стать инвесторами, но перед этим хотелось бы узнать финансовые показтели Вашей фирмы, ответье на несколько вопросов")
income = int(input("Введите Ваш доход:"))
spend = int(input("Введите Ваши расходы:"))
profit = income - spend
if income < spend:
    print("Я не ваш инвестор")
elif income <= spend:
    print("Старайся лучше! Возможно скоро я вернусь")
else:
    print("Вау, хочу знать секрет!")
Profitability = (profit / income) * 100
print(Profitability, "Ваша рентабельность")
staff = int(input("Укажите количество рабов в вашей компании?"))
efficancy = profit / staff
print (efficancy, "Настолько хороши сотрудники - каждый сделал свой вклад в прибыль компании")
