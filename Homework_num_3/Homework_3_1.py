def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'None / 0'
    except ValueError:
        return 'No value'


print(div((int(input('Введите первое число: '))), (int(input('Введите первое число: ')))))

