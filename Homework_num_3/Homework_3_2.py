def managelist(**kwargs):
    return list(kwargs.values())
print(managelist(name=input('Имя: '),
    sec_name=input('Фамилия: '),
    b_day=input('Дата рождения: '),
    town=input('Город проживания: '),
    email=input('Электронная почта: '),
    p_numb=input('Номер телефона: ')))
