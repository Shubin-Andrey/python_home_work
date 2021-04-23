class Cell:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __str__(self):
        out = ''
        for i in range(self.count):
            out += '*'
        self.out = out
        return out

    def __add__(self, other):
        out = self.count + other.count
        self.count = out

    def __sub__(self, other):
        if self.count > other.count:
            self.count -= other.count
        else:
            print('Невозможно провести вычитание')

    def __mul__(self, other):

        self.count *= other.count

    def __truediv__(self, other):

        self.count = self.count // other.count

    def make_order(self, nam):
        my_str = ''
        my_new_str = ''
        for i in range(self.count):
            my_str += '*'

        while len(my_str) > nam:
            my_new_str = my_new_str + my_str[:nam] + '\n'
            k = my_str[nam:]
            my_str = k
        my_new_str = my_new_str + my_str[:nam] + '\n'
        print(f'Отформатированный вывод клетки \n{my_new_str}')


first = Cell(1, 5)
second = Cell(2, 6)
print(f'{first}')
print(f'{second}')
first + second
print(f'Сложение 1 и 2 = {first}')
first = Cell(1, 5)
second = Cell(2, 6)
print(f'{first}')
print(f'{second}')
second - first
print(f'Вычитание 2 и 1 = {second}')
first = Cell(1, 5)
second = Cell(2, 6)
print(f'{first}')
print(f'{second}')
first - second
print(f'Вычитание 1 и 2 = {first}')
first = Cell(1, 5)
second = Cell(2, 6)
print(f'{first}')
print(f'{second}')
first * second
print(f'Умножение 1 на 2 = {first}')

first.make_order(4)

first = Cell(1, 5)
second = Cell(2, 6)
print(f'{first}')
print(f'{second}')
first / second
print(f'Деление 1 на 2 = {first}')
first = Cell(1, 5)
second = Cell(2, 6)
print(f'{first}')
print(f'{second}')
second / first
print(f'Деление 2 на 1 = {second}')
