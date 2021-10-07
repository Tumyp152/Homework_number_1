money_profit = int(input('Введите значение прибыли: '))
money_costs = int(input('Введите значение издержек: '))
workers = int(input('Ввдите количество работников: '))
if money_profit > money_costs:
    print('Выручка больше издержек')
    clear_profit = money_profit - money_costs
    rentbl = (clear_profit/money_profit)*100
    print('Рентабельность выручки {}: {:.2f}%' .format('составила', rentbl))
    cp_for_person = float(clear_profit/workers)
    print('Прибыль фирмы в расчете на одного сотрудника: %s'%cp_for_person)
elif money_profit == money_costs:
    print('Фирма проработала в ноль')
else:
    print('Фирма работает в убыток')