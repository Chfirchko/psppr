import numpy as np
import random
from matplotlib import pyplot as plt
ar = [[1, 3], [3, 3], [4, 3], [5, 3], [1, 2], [4, 2], [1, 1], [2, 1]]


m1 = [1, 1]
m2 = [2, 1]
k = 2
for zxc in range(0, 3):

    tab = []
    table = []
    for i in range(0, len(ar)):
        sum0 = (ar[i][0] - m1[0]) ** 2
        sum1 = (ar[i][1] - m1[1]) ** 2
        sum2 = (ar[i][0] - m2[0]) ** 2
        sum3 = (ar[i][1] - m2[1]) ** 2
        sum4 = np.sqrt(sum0 + sum1)
        sum5 = np.sqrt(sum2 + sum3)
        tab.append([sum4, sum5])
        if sum4 > sum5:
            tab.append(2)
        else:
            tab.append(1)
        table.append(tab)
        tab = []
    for i in table:
        print(i)
    sum0 = 0
    for i in range(0, len(ar)):
        if table[i][1] == 1:
            sum0 += table[i][0][0] ** 2
        else:
            sum0 += table[i][0][1] ** 2
    print('error =', sum0)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    n1 = 0
    n2 = 0
    for i in range(0, len(ar)):
        if table[i][1] == 1:
            sum1 += ar[i][0]
            sum3 += ar[i][1]
            n1 += 1
        else:
            sum2 += ar[i][0]
            sum4 += ar[i][1]
            n2 += 1
    sum1 = sum1 / n1
    sum2 = sum2 / n2
    sum3 = sum3 / n1
    sum4 = sum4 / n2
    print('centroids:', str(sum1) + ' ' + str(sum3), str(sum2) + ' ' + str(sum4), sep='\n')

    m1[0], m1[1] = sum1, sum3
    m2[0], m2[1] = sum2, sum4
    print()
plt.plot(ar, 'ro')
plt.plot(sum1, sum3, 'g^')
plt.plot(sum2, sum4, 'b^')
plt.show()