from time import sleep


class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def running(self):
        i = 0
        while i < 3:
            print('Цвет светофора: ', TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(8)
            i += 1


Lights = TrafficLight()
Lights.running()
