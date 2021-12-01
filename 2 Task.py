my_list = input("Введите элементы списка через пробел - ").split( )
if len(my_list) % 2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
else:
    my_list[:-1:2], my_list[1:-1:2] = my_list[1:-1:2], my_list[:-1:2]
print(my_list)
