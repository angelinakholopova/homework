#!/usr/bin/env python
# coding: utf-8

# **Задача 1**

# In[ ]:


n = int(input('Введите кличество монеток: '))
zero = 0
ones = 0
for i in range(n):
    a = int(input('Введите 0 или 1: '))
    if a == 1:
        ones += 1
    elif a == 0:
        zero += 1
    else: 
        print('Неверное значение!')
        
if ones >= zero:
    print(f'Минимальное число монеток, которое нужно перевернуть: {zero}')
else:
    print(f'Минимальное число монеток, которое нужно перевернуть: {ones}')

    


# **Задача 2**

# In[8]:


s = int(input('Сумма чисел: '))
p = int(input('Произведение чисел: '))
y = (s+(s*s-4*p)**(1/2))/2
x = s - y
print(f'Первое число: {x}; второе число: {y}')


# **Задача 3**

# In[11]:


n = int(input('Введите натуральное число: '))
m = 1
k = 1
while k < n:
    print(k)
    k = 2**m
    m += 1


# In[ ]:




