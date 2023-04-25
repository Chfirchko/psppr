# -*- coding: utf-8 -*-
import random
import numpy as np

file = open('1.txt', 'r', encoding='utf-8')
table = []
unique = []
for i in file:
    i = i.replace(',', '').replace('\n', '').lower().split(' ')
    i.pop(0)
    table.append(i)
    print(i)
print()
strings = []
for i in table:
    for j in i:
        strings.append(j)
strings = np.unique(strings)
strings1 = [1, 2, 3, 4, 5, 6, 7]
strings1[0] = strings[5]
strings1[1] = strings[6]
strings1[2] = strings[1]
strings1[3] = strings[2]
strings1[4] = strings[3]
strings1[5] = strings[0]
strings1[6] = strings[4]
strings = strings1
print(strings)
tab = np.zeros((14, 7))
i_tab = 0
j_tab = 0
for i in range(0, len(table)):
    if i == 0:
        pass
    else:
        i_tab += 1
    for j in range(0, len(table[i])):
        for z in range(0, len(strings)):
            qwer = strings[z]
            if strings[z] == table[i][j]:
                tab[i_tab][z] = 1
                break
print(tab)
sum = 0
sum0 = []
j = 0
for zxc in range(0, 7):
    for i in tab:
        if i[j] == 1:
            sum += 1
    print('F0', j, ' = ', sum, sep='')
    sum = 0
    j += 1
print()
sum = 0
st = ''
for j in range(0, len(strings)):
    for zxc in range(j+1, len(strings)):
        for i in range(0, len(tab)):
            if tab[i][j] == tab[i][zxc] == 1:
                st = str(j + 1) + str(zxc + 1)
                sum += 1
        print('F1_', st, ' = ', sum, sep='')
        a = sum
        sum0.append(a)
        sum = 0
    print()

print()
for i in sum0:
    if i >= 4:
        print(i)
print()
sum = 0
sum1 = []
st = ''

for qwe in range(0, len(strings)):
    for asd in range(qwe + 1, len(strings)):
        for zxc in range(asd + 1, len(strings)):
            for i in range(0, len(tab)):
                if tab[i][qwe] == tab[i][asd] == tab[i][zxc] == 1:
                    st = str(qwe) + str(asd) + str(zxc)
                    sum += 1
            if sum != 0:
                print('F2_', st, ' = ', sum, sep='')
            a = sum
            sum1.append(a)
            sum = 0
    print()
for i in sum1:
    if i >= 4:
        print(i)
print()