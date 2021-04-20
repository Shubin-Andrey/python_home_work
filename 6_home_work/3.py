class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, ' ', self.surname)

    def get_total_income(self):
        print(f'Прибыль сотрудника - {self._income["wage"] + self._income["bonus"]}')


a = Position('Ivan', 'Ivanov', 'datascintist', 2000, 1000)
a.get_full_name()
a.get_total_income()

b = Position('Nicolai', 'Nicolaev', 'worker', 1000, 500)
b.get_full_name()
b.get_total_income()
