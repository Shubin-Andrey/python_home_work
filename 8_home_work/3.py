new_list = []


class MyList:
    @classmethod
    def my_list_app(cls, arg):
        if arg.isdigit():
            new_list.append(arg)


print('Введите число, для завершения введите STOP')
count = False
while not count:
    a = input()
    if a.upper() == 'STOP':
        count = True
    else:
        MyList.my_list_app(a)
print(new_list)
