from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def cloth_calculation(self, size):
        pass


class Coat(Cloth):

    def __init__(self, size):
        self.v = size

    @property
    def cloth_calculation(self):
        s = int(self.v) / 6.5 + 0.5
        return f'Объем ткани неодходимый для шитья Пальто - {s}'


class Suit(Cloth):

    def __init__(self, size):
        self.v = size

    @property
    def cloth_calculation(self):
        s = (2 * self.v + 0.3)
        return f'Объем ткани неодходимый для шитья Костюма - {s}'


coat = Coat(30)
print(coat.cloth_calculation)

suit = Suit(30)
print(suit.cloth_calculation)
