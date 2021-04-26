class MyClass:
    @classmethod
    def my_devision(cls, arg1, arg2):
        try:
            print(arg1 / arg2)
        except ZeroDivisionError:
            print('Делить на 0 нельзя')


MyClass.my_devision(30, 0)
print('Программа отработала')
