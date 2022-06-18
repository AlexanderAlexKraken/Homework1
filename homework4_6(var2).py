from itertools import cycle

с = 0
for el in cycle("LIST"):
    if с > 11:
        break
    print(el)
    с += 1
