my_list = ["зима", "весна", "лето", "осень"]
i = int(input("Введите номер месяца - "))
if i == 1 or i == 2 or i == 12:
    print(my_list[0])
elif i == 3 or i == 4 or i == 5:
    print(my_list[1])
elif i == 6 or i == 7 or i == 8:
    print(my_list[2])
else:
    print(my_list[3])
