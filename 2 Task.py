def user_data(name, surname, birth_year, current_city, email, phone_number):
    return name, surname, birth_year, current_city, email, phone_number


first_name = input('Enter name: ')
second_name = input('Enter surname: ')
birth = input('Enter birth year: ')
city = input('Enter city: ')
mail = input('Enter email: ')
phone = input('Enter phone number: ')
print(user_data(first_name, second_name, birth, city, mail, phone))
