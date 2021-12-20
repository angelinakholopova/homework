my_list = [6, 38, 32, 1, 1, 76, 128, 55]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)
