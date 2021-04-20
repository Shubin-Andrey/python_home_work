class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.is_go = False

    def go(self, speed):
        self.is_go = True
        self.speed = speed
        print('Поехали со скоростью ', speed)

    def stop(self):
        self.is_go = False
        print('Остановились')

    def turn(self, direction):
        self.direction = direction
        if self.is_go == True:
            print(f'Машина повернула {self.direction}')
        elif self.is_go == False:
            print(f'Колеса повернули {self.direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60}')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40}')
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


zapor = WorkCar(60, 'Ржавый', '66', True)
zapor.go(80)
zapor.turn('Направо')
zapor.stop()
zapor.turn('Налево')
zapor.show_speed()
print('\n')
bugatti = TownCar(300, 'Грязный', 'Veiron', False)
bugatti.go(140)
bugatti.turn('Направо')
bugatti.stop()
bugatti.turn('Налево')
bugatti.show_speed()
print('\n')
uaz = PoliceCar(150, 'Белоголубой', 'Буханка', True)
zapor.go(200)
zapor.turn('Направо')
zapor.stop()
zapor.turn('Налево')
zapor.show_speed()
