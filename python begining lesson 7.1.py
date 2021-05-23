class Matrix:
    def __init__(self, p_1):
        self.matrix = p_1

    def __str__(self):
        matrix_str = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix_str += str(self.matrix[i][j]) + ' '
            matrix_str += '\n'
        return matrix_str

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += other.matrix[i][j]
        return Matrix(self.matrix)


if __name__ == '__main__':
    try:
        m_1 = Matrix([[1, 2, 3], [2, 3, 4]])
        print(m_1)
        m_2 = Matrix([[3, 4, 5], [3, 4, 5]])
        print(m_2)
        print(m_1 + m_2)
    except IndexError:
        print('Размер матриц задан неправильно')
