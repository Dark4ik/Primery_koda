'Лиличев Егор АА-21-07 Вариант №13 Задание 1_4'
import math

n = 3
m = 6
a = [[[0] for j in range(m)] for i in range(n)]
print('Исходная матрица А')
for i in range(n):
    for j in range(m):
        if i+j > 5:
            y = 1.473 + math.sqrt(0.39*j + i**2)
            a[i][j] = round(y, 3)
        else:
            y = math.cos((i-j) * math.pi/4 + math.exp(i+j))
            a[i][j] = round(y, 3)
        print(a[i][j], end='  ')
    print()



print('Преобразованная матрица')
k = 0
matrix = [[[0] for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = a[i][j]
        if matrix[i][j] < 0:
            k+=1;
            matrix[i][j] = 0
        print(matrix[i][j], end='  ')
    print()
print('Количество отрицательных элементов = ', k)

with open("vivod.txt", "w") as f:
    print('Ishod matrix A', file=f)
    for row in a:
        f.write(' '.join(map(str, row)) + '\n')
    print('Preobraz matrix A', file = f)
    for row in matrix:
        f.write(' '.join(map(str, row)) + '\n')
    print('Summa "-" elements ', k, file = f)