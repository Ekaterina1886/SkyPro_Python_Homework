n = int(input("Введите номер месяца от 1 до 12: "))
def month_to_season(n):
        if 3 <= n <= 5:
            print ("Весна")
        elif 6 <= n <= 8:
            print ("Лето")
        elif 9 <= n <= 11:
            print ("Осень")
        else:
            print ("Зима")
month_to_season(n)                    