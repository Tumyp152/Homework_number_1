cur_dist = float(input("Введите текущую дистанцию в километрах: "))
target_dist = float(input("Введите нужную дистанцию в километрах: "))
days = 0
while target_dist - cur_dist >= 0:
    cur_dist *= 1.1
    days += 1
print("Чтобы достичь нужной дистанции потребуется тренироваться {} дней " .format(days))