print("Снова здравствуйте! Помогите мне написать программу. Для ввода используйте числа. Мы узнаем сумму двух наибольших, из трех введеных Вами, чисел.")
# объявление функции
def max_sum(a, b ,c):
    if a >= b and a >= c:
        print(a)
    if b >= a and b >= c:
        print(b)
    elif c > a and c > b:
        print(c)

# считываем данные
numb_1 = int(input("Укажите первое число: "))
numb_2 = int(input("Укажите второе число: "))
numb_3 = int(input("Укажите третье число: "))
a = numb_1 + numb_2
b = numb_2 + numb_3
c = numb_1 + numb_3
# вызываем функцию
max_sum(a, b, c)

