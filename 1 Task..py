def division(num1, num2):
    num1 = int(input('Введите делимое: '))
    num2 = int(input('Введите делитель: '))
    if num2 == 0:
        return 'Нельзя делить на ноль!'
    else:
        return num1 / num2


division()
