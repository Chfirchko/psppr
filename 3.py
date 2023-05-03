
import numpy as np
import random
from matplotlib import pyplot as plt
import openpyxl as opl
file = opl.load_workbook('123.xlsx')
f = file.active
da = 0
net = 0
len = -1
for i in f:
    len += 1
    if i[4].value == 'Да':
        da += 1
    elif i[4].value == 'Нет':
        net += 1
print('Да:', da, 'Нет:', net, sep='\n')
print()
print('P(C2) = ', net / len)
print('P(C1) = ', da / len)
print()
n_net = 0
n_da = 0
dad = 1
nenet = 1
for i in f:
    if i[0].value == '<100' and i[4].value == 'Да':
        n_da += 1
print(n_da / da)
dad *= (n_da / da)
for i in f:
    if i[0].value == '<100' and i[4].value == 'Нет':
        n_net += 1
print(n_net / net)
nenet *= (n_net / net)
n_net = 0
n_da = 0
for i in f:
    if i[1].value == 'Средняя' and i[4].value == 'Да':
        n_da += 1
print(n_da / da)
dad *= (n_da / da)

for i in f:
    if i[1].value == 'Средняя' and i[4].value == 'Нет':
        n_net += 1
print(n_net / net)
nenet *= (n_net / net)
n_net = 0
n_da = 0
for i in f:
    if i[2].value == 'Средняя' and i[4].value == 'Да':
        n_da += 1
print(n_da / da)
dad *= (n_da / da)
for i in f:
    if i[2].value == 'Средняя' and i[4].value == 'Нет':
        n_net += 1
print(n_net / net)
nenet *= (n_net / net)
n_net = 0

n_da = 0
for i in f:
    if i[3].value == 'Да' and i[4].value == 'Да':
        n_da += 1
print(n_da / da)
dad *= (n_da / da)
for i in f:
    if i[3].value == 'Да' and i[4].value == 'Нет':
        n_net += 1
print(n_net / net)
nenet *= (n_net / net)
print()
print(dad, nenet)
print(dad * (da / len), nenet * (net / len))
print()
print(dad * (da / len) / (dad * (da / len) + nenet * (net / len)))
print(nenet * (net / len) / nenet * (net / len) + (dad * (da / len)))