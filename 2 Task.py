from abc import abstractmethod


class Clothes:

    def __init__(self, x):
        self.x = x

    @property
    @abstractmethod
    def expenditure(self):
        pass

    def __add__(self, other):
        return self.expenditure + other.expenditure


class Coat(Clothes):

    @property
    def expenditure(self):
        return self.x / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expenditure(self):
        return 2 * self.x + 0.3


coat = Coat(6)
suit = Suit(6)
print(suit + coat)
