my_list = [9, 9, 8, 7, 7, 7, 4, 2, 2, 2, 2, 1]
my_second_list = my_list.copy()
number = int(input('Введите число - '))
for i in range(len(my_list)):
  if number > my_list[i]:
    my_second_list.insert(i, number)
    break
  elif number < 2:
    my_second_list.append(number)
    break
print(my_second_list)