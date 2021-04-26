class ComplexNumber:

    def __init__(self, my_str):
        my_list = my_str.split()
        self.a = my_list[0]
        self.b = my_list[2][:-1]

    def __add__(self, other):
        sum_a = int(self.a) + int(other.a)
        sum_b = int(self.b) + int(other.b)
        return f'{sum_a} + {sum_b}i'

    def __mul__(self, other):
        mul_a = int(self.a) * int(other.a) - int(self.b) * int(other.b)
        mul_b = int(self.a) * int(other.b) + int(self.b) * int(other.a)
        return f'{mul_a} + {mul_b}i'


a = ComplexNumber('3 + 4i')

b = ComplexNumber('2 + 2i')

print(a + b)
print(a * b)
