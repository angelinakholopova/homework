class Matrix:
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    def __init__(self, matr):
        self.matr = matr

    def __add__(self, other):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        for i in range(len(self.matr)):
            for j in range(len(other.matr[i])):
                matrix[i][j] = self.matr[i][j] + other.matr[i][j]

        return '\n'.join(map(str, matrix))

    def __str__(self):
        m = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                m[i][j] = self.matr[i][j]
        return str('\n'.join(map(str, m)))


matr_1 = [[1, 1, 1],
          [2, 2, 2],
          [3, 3, 3]]
matr_2 = [[1, 2, 2],
          [2, 1, 2],
          [2, 2, 1]]

a = Matrix(matr_1)
b = Matrix(matr_2)
print(str(a))
print(str(b))
print(a + b)
