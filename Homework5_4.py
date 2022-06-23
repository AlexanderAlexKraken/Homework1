glossary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []
with open('new_file.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_text.append(glossary[i[0]] + '  ' + i[1])
    print(new_text)

with open('new_file_top.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_text)