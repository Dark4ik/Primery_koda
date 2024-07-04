from prettytable import PrettyTable
import math
import matplotlib.pyplot as plt
table = PrettyTable()
table.field_names = ["x", "Q", "z"]
def function(x):
    a = 0.35
    if abs(x) < 3:
        z = (a*x)/(x**2 + 2*x + 3)
    else:
        z = a/(x**2 - 2*x + 1)
    return math.asin(2*z)*math.log(z**2 + 1)

x_list = []
Q = []
z = []
k = 0
a = 0.35
for x in range(-5, 5+1, 2):
    x_list.append(x)
    Q.append(function(x))
    k += 1

for x in x_list:
    if abs(x) < 3:
        zi = (a*x)/(x**2 + 2*x + 3)
        z.append(zi)
    else:
        zi = a/(x**2 - 2*x + 1)
        z.append(zi)

for i in range(len(z)):
    table.add_row([x_list[i], Q[i], z[i]])

print(table)
# Прорисовка графика
ax = plt.axes()
ax.set_facecolor("grey")        # установка фона
ax.set_xlabel('ось x')          # создание наименование графика по оси х
ax.set_ylabel('ось y')          # создание наименование по оси у
ax.spines['right'].set_color('none')    # Убираем правую ось
ax.spines['top'].set_color('none')      # Убираем верхнюю ось
# ax.spines['left'].set_position('zero')      # Передвигаем левую ось на ноль
# ax.spines['bottom'].set_position('zero')    # Передвигаем нижнюю ось на ноль
# ax.xaxis.set_ticks_position('bottom')     # Перемещаем деления на ось OX
# ax.yaxis.set_ticks_position('left')       # Перемещаем деления на ось OY
plt.plot(x_list, Q, marker="o", label='Q(x)', color='blue', markerfacecolor="black")
plt.plot(x_list, z, '-', label='Z(x)', color='red', marker='o', markerfacecolor="white")
plt.grid(True, color='0.95')    # сетка
plt.title("График функции")     # название графика
plt.legend(title="Легенда:")    # инициализация легенды

plt.show()