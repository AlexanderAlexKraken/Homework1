list = input ('Введите произвольные слова через пробел:').split()
for ind, el in enumerate(list):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(ind,el[0:10])