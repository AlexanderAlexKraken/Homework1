print("У нас новое задание. Попробуем разобраться в числах. Будем сортировать их по местам, в порядке возрастания или убывания.")
my_list = [3, 5, 7, 3, 2]
new_list = int(input("Введи число:"))
my_list.append(new_list)
n = []
while len(my_list) > 0:
    n.append(max(my_list))
    my_list.remove(max(my_list))
print(n)