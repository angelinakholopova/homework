class Date:

  def __init__(self, date):
    self.date = str(date)

  @classmethod
  def strtoint(cls, date):
      dates = []
      for i in date.split():
          if i != '-':
              dates.append(i)
        return int(dates[0]), int(dates[1]), int(dates[2])

  @staticmethod
  def validation(day, month, year):
    if day <= 0 or day > 31:
      print('Неверно введена дата!')
    elif month < 1 or month > 12:
      print('Неверно введен месяц!')

print(Date.strtoint('27-6-2002'))
birtyday = Date('26-4-2000')
print(birtyday)
Date.validation(27, 6, 2002)
