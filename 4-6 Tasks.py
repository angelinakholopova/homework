class Storage:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return self.name, 'Price', self.price, 'Quantity', self.quantity

    def reception(self):
        try:
            unit = input('Enter name ')
            unit_p = int(input('Enter price '))
            unit_q = int(input('Enter quantity '))
            unique = {'Model': unit, 'Price': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print('Current list - ', self.my_store)
        except:
            return 'Error'

        print('For exit - Q, for continue - Enter')
        q = input('---> ')
        if q == 'Q':
            self.my_store_full.append(self.my_store)
            print('All storage - ', self.my_store_full)
            return 'Exit'
        else:
            return Storage.reception(self)


class Printer(Storage):
    def to_print(self):
        return 'to print smth', self.numb, 'times'


class Scanner(Storage):
    def to_scan(self):
        return 'to scan smth', self.numb, 'times'


class Copier(Storage):
    def to_copier(self):
        return 'to copier smth', self.numb, 'times'


unit_1 = Printer('hp', 2000, 10, 10)
unit_2 = Scanner('Canon', 4200, 5, 5)
unit_3 = Copier('Xerox', 1500, 10, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())