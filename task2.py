from matplotlib import pyplot as plt
from random import randint

arr = [randint(1, 100) for i in range(randint(1, 20))]
n = len(arr)

print("Случайный набор данных:", *arr)

amount_num = {}
for i in arr:
    if i in amount_num.keys():
        amount_num[i] += 1
    else:
        amount_num[i] = 1

probability = 0
arr_set = list(set(arr))
for i in arr_set:
    probability += i * (amount_num[i] / n)

print("Математическое ожидание для этого набора равно -", probability)

dispersion = 0
probability2 = 0
for i in arr_set:
    probability2 += i * i * (amount_num[i] / n)
dispersion = probability2 - probability ** 2
sredn_otkl = dispersion ** 0.5

print("Среднеквадратичное отклонение равно -", sredn_otkl)

x = arr
y = [randint(1, 100) for i in range(n)]
x_y, sum_x, sum_y, x_2 = 0, 0, 0, 0
for i in range(n):
    x_y += x[i] * y[i]
    sum_x += x[i]
    sum_y += y[i]
    x_2 += x[i] ** 2
a, b = 0, 0
if n * x_2 != sum_x ** 2:
    a = (n * x_y - sum_x * sum_y) / (n * x_2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
else:
    print("Невозможно построить прямую")

x1, x2 = min(x), max(x)
y1, y2 = a * x1 + b, a * x2 + b
plt.scatter(x, y)
plt.plot([x1, x2], [y1, y2])
plt.show()