class Road:
    def __init__(self, __length, __width):
        self.lenght = __length
        self.width = __width

    def build_road(self, mass_metr, hight):
        self.mass_metr = mass_metr
        self.hight = hight
        all_mass = self.hight * self.mass_metr * self.width * self.lenght
        print(all_mass)


a = Road(5000, 20)
a.build_road(25, 5)
