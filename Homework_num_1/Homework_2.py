sec = int(input('Введите время в секундах: '))
h = ((sec // 3600)) % 24
m = (sec // 60) % 60
s = sec % 60
print('{0}:{1:=02}:{2:=02}'.format(h, m, s))