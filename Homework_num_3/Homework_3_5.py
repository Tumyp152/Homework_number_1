def hw5():
    res = 0
    while True:
        nums = input('Введите список чисел, или ! чтобы завершить: ').split()
        for i in nums:
            try:
                if i == '!':
                    print(f'Сумма: {res}. Завершение.')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите число или !')
        print(f'Сумма: {res}')
hw5()