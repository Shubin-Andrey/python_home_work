class Store:
    store_equipment = {}

    def __init__(self, total_store, adress):
        self.total_store = total_store
        self.adress = adress

    def store_add(self, eqp, count):
        self.store_equipment[eqp] = count
        self.total_store -= count * int(eqp.volume)

    def store_sub(self, eqp, count):
        self.store_equipment.pop(eqp)
        self.total_store += count * int(eqp.volume)


class OfficeEquipment:
    def __init__(self, name, price, volume):
        self.name = name
        self.price = price
        self.volume = volume

    def __str__(self):
        return self.name


class Printer(OfficeEquipment):
    color = 'white'


class Scaner(OfficeEquipment):
    smark = 'hp'


class Kserox(OfficeEquipment):
    brash_color = 'rad'


first = Store(2000, 'asd')

a = Printer('hp', 20000, 20)

first.store_add(a, 5)
print(first.store_equipment, first.total_store)
first.store_sub(a, 5)
print(first.store_equipment, first.total_store)
