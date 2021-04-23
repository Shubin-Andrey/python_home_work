class Matrix:
    def __init__(self, my_list):
        self.matrix_list = my_list

    def __str__(self):
        for el in self.matrix_list:
            print(el)
        return '\n'
        # return f'{self.matrix_list[0]}\n{self.matrix_list[1]}\n{self.matrix_list[2]}'

    def __add__(self, other):  # Скажу честно: не смог сделать через генераторы.
        i = 0

        new_list = []
        while i < len(self.matrix_list):
            new_list_cikl = []
            for j in range(len(self.matrix_list[i])):
                new_list_cikl.append(self.matrix_list[i][j] + other.matrix_list[i][j])
            i += 1
            new_list.append(new_list_cikl)
        return new_list


a = Matrix([[1, 2, 3, 4], [4, 5, 6, 3], [7, 8, 9, 2], [7, 8, 9, 7]])
b = Matrix([[9, 8, 7, 1, 1], [6, 5, 4, 1, 1], [3, 2, 1, 1, 1], [7, 8, 9, 1, 1]])
print(a)
print(b)
c = Matrix(a + b)
print(c)
