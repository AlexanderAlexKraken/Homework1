with open('count_file.txt', 'w') as file_obj:
    line = input('Введите цифры через пробел:')
    file_obj.writelines(line)
    my_numb = line.split()
    print(sum(map(int, my_numb)))
