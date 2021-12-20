class Road:

    def __init__(self, length, width, density, thickness):
        self._length = length
        self._width = width
        self.density = density
        self.thickness = thickness

    def mass(self):
        massa = self._length * self._width * self.density * self.thickness
        print(
        'Масса асфальта = ', self._length, ' * ', self._width, ' * ', self.density, ' * ', self.thickness, ' = ', massa)


pavement = Road(20, 5000, 25, 5)
pavement.mass()
