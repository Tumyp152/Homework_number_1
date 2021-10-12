def max2nums(a, b, c):
    n = [a, b, c]
    n.remove(min(a, b, c))
    return sum(n)
print("Сумма двух максимальных чисел равна:", max2nums(int(input("Первое число: ")), int(input("Второе число: ")), int(input("Третье число: "))))
