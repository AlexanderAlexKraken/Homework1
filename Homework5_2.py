new_list = ['Hello\n','New hello\n', 'New new hello\n']
with open("domashka.txt", "w") as obj:
    obj.writelines(new_list)
with open('domashka.txt') as obj:
    spisok = 0
    for i in obj:
        slova = 0
        spisok += i.count('\n')
        slova += i.count(' ')
        print(f'{slova+1} слов в строке')
    print(f'В файле {spisok} строки')