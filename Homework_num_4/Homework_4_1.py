def zbrstv():
    h_all = float(input('Введите сколько часов отработал сотрудник: '))
    p1h = float(input('Введите сумму оплаты за 1 час: '))
    prm = float(input('Укажите размер премии: '))
    pay = h_all * p1h
    return pay + prm
print(f'Размер заработной платы составил: {zbrstv() }')