def my_func(num1, num2, num3):
    if num1 >= num3 and num2 >= num3:
        return num1 + num2
    elif num1 >= num2 and num3 >= num2:
        return num1 + num3
    elif num2 >= num1 and num3 >= num1:
        return num2 + num3


num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
num_3 = int(input('Enter third number: '))
print(my_func(num_1, num_2, num_3))
