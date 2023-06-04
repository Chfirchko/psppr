import numpy as np
import random
from matplotlib import pyplot as plt



table = [[13, 1000, 1323.4, 0],
         [20, 600, 305.6, 1],
         [17, 500, 741.8, 0],
         [15, 1200, 1032.6, 1],
         [16, 1000, 887.2, 1],
         [12, 1500, 1468.8, 1],
         [16, 500, 887.2, 0],
         [14, 1200, 1178.0, 1],
         [10, 1700, 1759.6, 0],
         [11, 2000, 1614.2, 1]
         ]
table1 = [13, 20, 17, 15, 16, 12, 16, 14, 10, 11]
table2 = [1000, 600, 500, 1200, 1000, 1500, 500, 1200, 1700, 2000]


sum1 = 0
for i in table1:
    sum1 += i ** 2
array = np.array([[len(table), sum(table1)], [sum(table1), sum1]])
sum2 = 0
for i in range(len(table2)):
    sum2 += table2[i] *  table1[i]
array1 = np.array([sum(table2), sum2])
print(array, array1)
res = np.linalg.solve(array, array1)
print(res)
sum3 = 0
for i in range(10):
    a = table[i][2]
    b = table[i][1]
    sum3 += (a - b) ** 2
print(sum3, len(table))
Ecko = sum3 / (len(table) - 1 - 1)
print('Ecko =', Ecko)
Sqrt_Ecko = np.sqrt(Ecko)
print('Ect =', Sqrt_Ecko)
plt.plot(table1, table2, 'ro')
x = np.linspace(5, 22, 250)
y1 = res[1] * x + res[0] + Sqrt_Ecko
y2 = res[1] * x + res[0] - Sqrt_Ecko
y = res[1] * x + res[0]
# Построение графика
corr_coef = np.corrcoef(x, y2)
print(corr_coef)
plt.plot(x, y1, 'r')
plt.plot(x, y2, 'b')
plt.plot(x, y, 'g')
plt.show()