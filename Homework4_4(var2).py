from itertools import count

my_list = [2, 4, 8, 8, 8, 8, 10, 123, 123, 123, 55, 76, 666, 87, 666, 666, 555, 555, 35]
new_my_list = [el for el in my_list if my_list.count(el) == 1]
print(my_list)
print(new_my_list)


