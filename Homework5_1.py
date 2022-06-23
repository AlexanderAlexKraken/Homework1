new_list = []
while True:
    new_text = input('Insert text: ')
    if new_text == '':
        print(new_list)
        exit()
    else:
        new_text_update = new_text
        new_list.append(new_text_update)

f_obj = open('new_file.txt', 'w')
f_obj.writelines(new_list)
f_obj.close()