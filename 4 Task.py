class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина едет!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        if direction == 'right':
            print('Машина повернула направо!')
        elif direction == 'left':
            print('Машина повернула налево!')

    def show_speed(self):
        print('Скорость автомобиля составляет: ', self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Внимание! Вы превысили скорость!')
        else:
            print('Вы едете по правилам!')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Внимание! Вы превысили скорость!')
        else:
            print('Вы едете по правилам!')


class SportCar(Car):

    def wow_sport(self):
        print('Вау у вас спортивная машина!!')


class PoliceCar(Car):

    def isitpolice(self):
        if self.is_police == True:
            print('Круто! Вы следите за законом! Не переусердствуйте!')
        else:
            print('Вы не полицейский!')


ferrari = SportCar(300, 'red', 'Феррари', False)
ferrari.wow_sport()
golf = TownCar(70, 'grey', 'Фольксваген', False)
golf.show_speed()
truck = WorkCar(30, 'white', 'Грузовик', False)
truck.show_speed()
police = PoliceCar(50, 'blue', 'Полицейчкая машина', True)
police.isitpolice()
not_police = PoliceCar(50, 'blue', 'Не полицейчкая машина', False)
not_police.isitpolice()
zhiguli = Car(50, 'purple', 'Жигули', False)
zhiguli.show_speed()
