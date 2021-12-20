class Cell:
  def __init__(self, numofcell):
    self.numofcell = numofcell

  def __add__(self, other):
    return self.numofcell + other.numofcell

  def __sub__(self, other):
    if self.numofcell < other.numofcell:
      print('Невозможно выполнить операцию вычитание!')
    else:
      return self.numofcell - other.numofcell

  def __mul__(self, other):
    return int(self.numofcell * other.numofcell)

  def __truediv__(self, other):
    return self.numofcell // other.numofcell

  def make_order(self, numinrow):
    row = ''
    for i in range(int(self.numofcell / numinrow)):
      row += f'{"*" * numinrow} \\n'
    row += f'{"*" * (self.numofcell % numinrow)}'
    return row

cells1 = Cell(33)
cells2 = Cell(9)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells1 * cells2)
print(cells1 / cells2)
print(cells2.make_order(5))
print(cells1.make_order(10))