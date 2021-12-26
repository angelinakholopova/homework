class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, ' + ', self.y + other.y, ' * i'

    def __mul__(self, other):
        return self.x * other.x - self.y * other.y, '+', self.x * other.y +self.y * other.x, ' * i'


z1 = Complex(2, 3)
z2 = Complex(3, 3)
print(z1 + z2)
print(z1 * z2)
