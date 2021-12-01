string = input('Введите строку - ').split( )
for i in range(len(string)):
  print(i + 1, string[i][:10])