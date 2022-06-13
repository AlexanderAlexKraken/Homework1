print("Доброго времени суток! У нас новое задание, изучаем 3 урок. В данном задании требуется ввести два числа и узнать частное отделения")

def s_calc():
    try:
        num_1 = float(input("Укажите первое число: "))
        num_2 = float(input("Укажите второе число: "))
    except ValueError:
        return
    result = num_1 / num_2
    return result

print(s_calc())