class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашем.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')


a = Stationery('a')
a.draw()
print('\n')
p = Pen('p')
p.draw()
print('\n')
p_e = Pencil('p_e')
p_e.draw()
print('\n')
h = Handle('h')
h.draw()
