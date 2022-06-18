from math import factorial

#print(f"factorial() -> {factorial(4)}")

def my_gen_factorial(n):
    el = 1
    for i in range(1, n + 1):
        el *= i
    yield el
a = my_gen_factorial(4)
a
for i in a:
    print(i)

#print(factorial(4))
#print(factorial(6))
