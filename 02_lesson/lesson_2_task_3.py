from math import ceil

def square(a):
    area = a * a
    return ceil (area)
a = float(input("Введите значение а =  "))
print(f"Площадь квадрата равна {square(a)}")