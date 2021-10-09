inp_val = int(input("Введите число: "))
out_val = inp_val % 10
inp_val = inp_val // 10
while inp_val > 0:
    if inp_val % 10 > out_val:
        out_val = inp_val % 10
    inp_val = inp_val // 10
print("Максимальная цифра в числе равна: ", out_val)