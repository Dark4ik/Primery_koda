'Лиличев Егор АА-21-07 Вариант №13 Задание 1_3'
import math
m = int(input("Если хотите решить выражение с константами, напишите 1. В другом случае 0: "))
if m == 1:
    x = -4.5
    y = 0.75
    z = 0.845
    a = (math.sqrt(8+(abs(x-y))**2+1.5*x))/(x**2+y**2+2)
    b = math.exp(abs(x-y))*((math.tan(z)**2+1)**x)
    print('a = %.3f' % a)
    print('b = %.3f' % b)
elif m == 0:
    x = float(input("Введите первое значение: "))
    y = float(input("Введите второе значение: "))
    z = float(input("Введите третье значение: "))
    a = (math.sqrt(8 + (abs(x - y)) ** 2 + 1.5 * x)) / (x ** 2 + y ** 2 + 2)
    b = math.exp(abs(x - y)) * ((math.tan(z) ** 2 + 1)**x)
    print('a = %.3f' % a)
    print('b = %.3f' % b)
