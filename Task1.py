class Matrix:

    def __init__(self, m):
        self.matrix = m

    def __str__(self):
        temp = ""
        for el in self.matrix:
            out = "\t".join(map(str, el))
            temp += out + "\n"
        return temp

    def __add__(self, other):
        temp1 = []
        for i, el1 in enumerate(self.matrix):
            temp2 = []
            for j, el2 in enumerate(self.matrix[i]):
                temp2.append(self.matrix[i][j] + other.matrix[i][j])
            temp1.append(temp2)
        return Matrix(temp1)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1 + matrix_2)
