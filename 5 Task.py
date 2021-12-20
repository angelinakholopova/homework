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
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером.')


red_pen = Pen('красная ручка')
red_pen.draw()
blue_pencil = Pencil('красная ручка')
blue_pencil.draw()
black_handle = Handle('красная ручка')
black_handle.draw()
red_pencil = Stationery('красная ручка')
red_pencil.draw()
