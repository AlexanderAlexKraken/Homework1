line = (input('Введите числа через пробел: '))
str_list = line.split(' ')
str_list
def str_to_num(str):
    str = str.strip()
    if '.' in str and str.replace('.', '').isdigit():
        return float(str)
    elif str.isdigit():
        return int(str)
    elif str.istitle():
        return ValueError
    return None

num_list = []
for i in str_list:
    n = str_to_num(i)
    if n is not None:
        num_list.append(str_to_num(i))
num_list
print(sum(num_list))