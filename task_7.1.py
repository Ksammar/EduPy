# + Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

# from copy import deepcopy

class Matrix:
    def __init__(self, matr):
        # self.data = deepcopy(matr)
        self.data = matr
        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def __str__(self):
        res = ''
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                res += str(self.data[i][j]) + ' '
            res += '\n'
        return res
        # нашёл однострочное решение, но не до конца понял как оно работает, поэтому реализовал сложнее...
        # return '\n'.join('\t'.join(map(str, row)) for row in self.data)

    def __getitem__(self, item):
        return self.data[item]

    def size(self):
        return (self.rows, self.cols)

    def __add__(self, other):
        result = []
        if self.eq_size(other):
            for i in range(len(self.data)):
                str_matr = []
                for j in range(len(self.data[0])):
                    summa = self.data[i][j] + other.data[i][j]
                    str_matr.append(summa)
                result.append(str_matr)
            return Matrix(result)
        else:
            print('Попытка сложения матриц разного размера!')
            return None

    def __sub__(self, other):
        result = []
        if self.eq_size(other):
            for i in range(len(self.data)):
                str_matr = []
                for j in range(len(self.data[0])):
                    summa = self.data[i][j] - other.data[i][j]
                    str_matr.append(summa)
                result.append(str_matr)
            return Matrix(result)
        else:
            print('Попытка вычитания матриц разного размера!')
            return None

    def __mul__(self, other):
        result = []
        if self.cols == other.rows:
            for i in range(len(self.data)):
                str_matr = []
                for j in range(len(other.data[0])):
                    summa = 0
                    for k in range(len(self.data[0])):
                        summa += self.data[i][k] * other.data[k][j]
                    str_matr.append(summa)
                result.append(str_matr)
            return Matrix(result)
        else:
            print('Попытка перемножения матриц несоответствующего размера!')
            return None

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    # def __eq__(self, other):

    def eq_size(self, other):
        if (self.rows == other.rows) and (self.cols == other.cols):
            return True
        else:
            return False


# m1 = Matrix([[1, 2, 3], [-1, 0, 1], [0, 0, 1]])
# m2 = Matrix([[-10, -20, -30], [10, 0, -10], [0, 0, -10]])
# m3 = Matrix([[1, 2, 3], [-1, 0, 1]])
# print(m1 + m2)
# print(m1 + m3)
# print(m1 - m2)
# m1 += m2
# print(m3.size())
# print(m3)
# print(m1[0][2])
m1 = Matrix([[1, 2, 4], [3, -3, 0]])
# m2 = Matrix([[1, -1, -1], [0, 1, 7], [1, 3, 10]])
m2 = Matrix([[1], [-2], [3]])
print(m1 * m2)
m1 = Matrix([[1, 2, 3], [-1, 0, 1], [0, 0, 1]])
m2 = Matrix([[-10, -20, -30], [10, 0, -10], [0, 0, -10]])
print(m1 + m2)
print(m1 * m2)
m3 = Matrix([[1, 2, 3], [-1, 0, 1]])
print(m1 * m3)
