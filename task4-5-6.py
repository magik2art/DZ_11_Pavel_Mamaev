class Warehouse:
    pass


class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Введите наименование устройства: ')
            price = int(input(f'Введите цену устройства в рублях за 1 штуку: '))
            quantity = int(input(f'Введите количество товара которое нужно принять на склад: '))
            item = {'Наименование устройства': name, 'Цена за штуку': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class VacumCleaner(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


p = VacumCleaner('Hobot', 1, 22990)
s = Scanner('Canon', 1, 1000)
x = Xerox('Xerox', 1, 15000)
p.income()
s.income()
x.income()
