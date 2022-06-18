my_list = [2, 1, 10, 4, 100, 50, 22, 6]
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
