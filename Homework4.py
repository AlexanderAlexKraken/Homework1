print("И снова здравствуйте! У нас новое задание - теперь требуется ввести целое положительное число"
      " а программа найдет самую большую цифру в числе")
n = 0
number = int(input("Введите любое целое положительное число: "))
while number != 0:
    last_digit = number % 10
    if last_digit > n:
        n = last_digit
    number = number // 10
print (n)