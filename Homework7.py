print("Перейдем к с портивным занятиям! Узнаем успехи нашего спортсмена, на какой день он смог стать лучшим, при условии, что каждые день он смог бегать на 10 % больше.")
a = int(input("Введите количество расстояния в километрах, с чего начинал наш спортсмен:"))
b = int(input("Введите количество расстояния в километрах, к которому наш спортсмен стремится:"))
counter = 1
while a <= b:
    counter += 1
    x = (a * 10) / 100
    a = a + x
print( "Ура, поздравляем, на ", counter, "день Вы достигли результата и пробегаете не менее", b, "км!")