class Store:
    store_equipment = []

    def __init__(self, total_store, adress):
        self.total_store = total_store
        self.adress = adress

    def store_add(self, eqp):
        self.store_equipment.append(eqp)


class OfficeEquipment:
    def __init__(self, name, price, volume):
        self.name = name
        self.price = price
        self.volume = volume


class Printer(OfficeEquipment):
    color = 'white'


class Scaner(OfficeEquipment):
    smark = 'hp'


class Kserox(OfficeEquipment):
    brash_color = 'rad'


first = Store(200, 'asd')

a = Printer('hp', 20000, 20)

first.store_add(a)
