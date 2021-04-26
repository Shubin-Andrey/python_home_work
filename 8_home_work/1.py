class MyDate:
    def __init__(self, new_date):
        self.new_date = new_date

    @classmethod
    def get_date(cls, new_date):
        my_dict = {}
        fail_list = []
        my_list = new_date.split(':')

        try:
            my_dict['День'] = int(my_list[0])
        except ValueError:
            fail_list.append('День не является числом')

        try:
            my_dict['Месяц'] = int(my_list[1])
        except ValueError:
            fail_list.append('Месяц не является числом')

        try:
            my_dict['Год'] = int(my_list[2])
        except ValueError:
            fail_list.append('год не является числом')

        if fail_list:
            print(fail_list)
            return None

        print(my_dict)

    @staticmethod
    def my_validation(new_date):
        fail_list = []
        my_list = new_date.split(':')
        if not my_list[0].isdigit():
            fail_list.append('День должен быть числом')

        elif not 0 <= int(my_list[0]) <= 31:
            fail_list.append('День находится в недопустимом диапазоне ')

        if not my_list[1].isdigit():
            fail_list.append('Месяц должен быть числом')

        elif not 0 <= int(my_list[1]) <= 12:
            fail_list.append('Месяц находится в недопустимом диапазоне ')

        if not my_list[2].isdigit():
            fail_list.append('Год должен быть числом')

        if fail_list:
            print(fail_list)
            return None

        print('Дата прошла валидацию')


MyDate.get_date(input('Введите дату формата дд:мм:гг'))
MyDate.my_validation(input('Введите дату дд:мм:гг'))
