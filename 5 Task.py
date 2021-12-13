from functools import reduce


def mult(prev_el, el):
    return prev_el * el


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(mult, my_list))
