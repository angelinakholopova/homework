# coding=utf-8
with open('1_file.txt', 'w+') as f:
    line = input('Введите строку в файл, для прекращения записи нажмите enter: ')
    while line:
        f.writelines(line)
        line = input('Введите строку в файл, для прекращения записи нажмите enter: ')
    f.seek(0)
    print(f.read())
