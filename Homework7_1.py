# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
import copy

class Matrix:
    def __init__(self, matrix):
       self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
           return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)

l1 = [[2, 4, 4], [7, 7, 7], [6, 6, 6]]
l2 = [[10, 20, 40], [30, 11, 48], [76, 6, 86]]
m = Matrix(l1)
s = Matrix(l2)
z = m + s
print(z)
print(Matrix(l1))
print(type(z))