list = input ('Введите произвольные числа, слова:').split()
print(list)
for el in range(0, len(list) -1, 2):
    list[el], list[el+1]=list[el+1], list[el]
print(list)