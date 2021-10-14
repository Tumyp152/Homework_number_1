int1 = 15
float1 = 15.7
str1 = "Привет"
list1 = ['Меня зовут Тимур', '2']
tuple1 = ('Мне 15 лет', '3')
dict1 = {'Страна': 'Казахстан', 'Город': 'Кызылорда'}
list2 = [int1, float1, str1, list1, tuple1, dict1]
for i in list2:
    print(f'{i} is {type(i)}')