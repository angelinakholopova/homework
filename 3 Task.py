class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        print('Полное имя сотрудника: ', self.name, self.surname)

    def get_total_income(self):
        income = int(self._income["wage"]) + int(self._income["bonus"])
        print('Доход: ', income)


director = Position('Elon', 'Musk', 'Director', 1000000, 500000)
director.get_full_name()
director.get_total_income()
