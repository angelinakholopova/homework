class Exeption:
    def __init__(self, *args):
        self.my_list = []

    def listint(self):
        while True:
            try:
                param = int(input('Enter an integer, to exit enter q - '))
                self.my_list.append(param)
                print('Now your list looks like: ', self.my_list)
            except:
                if param == 'q':
                    print('Your end list looks like: ', self.my_list)
                    break

                else:
                    print('Unsuitable type of parameter has been entered')
                    param2 = int(input('Enter an integer, to exit enter q - '))
                    self.my_list.append(param2)
                    print('Now your list looks like: ', self.my_list)


try_except = Exeption(1)
print(try_except.listint())
