import math
def square(a):
    area = a * a
    return math.ceil (area)
a = int(input("Введите значение а =  "))
print(f"Площадь квадрата равна {square(a)}")
