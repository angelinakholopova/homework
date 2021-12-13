with open('3_file.txt', 'r') as f:
  name = []
  sal = []
  my_list = f.read().split('\n')
  for i in my_list:
    i = i.split( )
    if int(i[1]) < 20000:
      name.append(i[0])
    sal.append(int(i[1]))
    avarage = sum(sal) / len(sal)
  print(f'{name}\n{avarage}')