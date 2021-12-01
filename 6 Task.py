products = int(input('Введите количество товаров - '))
my_list = []
analytics = {
    "название" : [],
    "цена" : [],
    "количество" : [],
    "ед" : [],
}
for i in range(products):
  my_dict = {
      "название" : input("Введите название товара - "),
      "цена" : input("Введите цену товара - "),
      "количество" : input("Введите количество товаров - "),
      "ед" : input("Введите единицы измерения - "),
             }
  my_list.append((i + 1, my_dict))
  for field in my_dict:
    for details in analytics:
      if field == details:
        analytics[details].append(my_dict[field])
print(my_list)
print(analytics)
