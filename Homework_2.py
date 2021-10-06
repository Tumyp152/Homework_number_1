time_all = input("Введите нужное число секунд:  ")
temp_int = int(time_all) % 3600
time_hours = int(time_all) // 3600
time_min = int(temp_int) // 60
time_sec = int(temp_int) % 60
print("Общее время: ", time_hours, ":", time_min, ":", time_sec)

