#!/usr/bin/env python
# coding: utf-8

# **Задача 1.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.**

# In[3]:


n = int(input('Введите количество элементов в массиве: '))
A = []
for i in range(n):
    k = int(input('Введите элемент массива: '))
    A.append(k)
X = int(input('Введите искомое число: '))
print(f'Число {X} повторяется {A.count(X)}')


# **Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.**

# In[5]:


n = int(input('Введите количество элементов в массиве: '))
A = []
for i in range(n):
    k = int(input('Введите элемент массива: '))
    A.append(k)
X = int(input('Введите искомое число: '))
step = abs(A[0] - X)
closest = A[0]
for i in A:
    if abs(i - X) < step:
        step = abs(i - X)
        closest = i
        
print(f'Ближайшее к {X} число - {closest}')
    


# **Задача 3.
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка;B, C, M, P – 3 очка;F, H, V, W, Y – 4 очка;K – 5 очков;J, X – 8 очков;Q, Z – 10 очков.А русские буквы оцениваются так:А, В, Е, И, Н, О, Р, С, Т – 1 очко;Д, К, Л, М, П, У – 2 очка;Б, Г, Ё, Ь, Я – 3 очка;Й, Ы – 4 очка;Ж, З, Х, Ц, Ч – 5 очков;Ш, Э, Ю – 8 очков;Ф, Щ, Ъ – 10 очков.Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.**

# In[1]:


dict_eng = {1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
           2 : ['D', 'G'],
           3 : ['B', 'C', 'M', 'P'],
           4 : ['F', 'H', 'V', 'W', 'Y'],
           5 : ['K'],
           8 : ['J', 'X'],
           10 : ['Q', 'Z']}
dict_rus = {1 : ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
           2 : ['Д', 'К', 'Л', 'М', 'П', 'У'],
           3 : ['Б', 'Г', 'Ё', 'Ь', 'Я'],
           4 : ['Й', 'Ы'],
           5 : ['Ж', 'З', 'Х', 'Ц', 'Ч'],
           8 : ['Ш', 'Э', 'Ю'],
           10 : ['Ф', 'Щ', 'Ъ']}
word = input('Введите слово: ')
score = 0
word = word.upper()
p = len(word) - 1
while p > 0:
    for key, value in dict_eng.items():
        for j in value:
            if word[p] == j:
                score += key
                p -= 1
print(score)

