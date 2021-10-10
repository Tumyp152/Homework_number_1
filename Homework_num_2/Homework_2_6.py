goods = []
while input("Вы хотите добавить продукт? Введите y/n: ") == 'y':
    number = int(input("Введите номер продукта: "))
    features = {}
    while input("Хотите добавить параметры продукта? Введите y/n: ") == 'y':
        product_name = input("Введите название продукта: ")
        price = input("Введите цену продукта: ")
        features[product_name] = price
    goods.append(tuple([number, features]))
print(goods)
#goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]

analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(" ")
print(analitics)