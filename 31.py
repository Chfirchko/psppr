import numpy as np
import random
from matplotlib import pyplot as plt

table = [['<100', 'Высокая', 'Средняя', 'Нет', 'Да', ],
         ['<100', 'Высокая', 'Высокая', 'Нет', 'Да', ],
         ['100-150', 'Высокая', 'Средняя', 'Нет', 'Нет', ],
         ['>150', 'Средняя', 'Средняя', 'Нет', 'Да', ],
         ['>150', 'Низкая', 'Средняя', 'Да', 'Нет', ],
         ['>150', 'Низкая', 'Высокая', 'Да', 'Нет', ],
         ['100-150', 'Низкая', 'Высокая', 'Да', 'Да', ],
         ['<100', 'Средняя', 'Средняя', 'Нет', 'Нет', ],
         ['<100', 'Низкая', 'Средняя', 'Да', 'Да', ],
         ['>150', 'Средняя', 'Средняя', 'Да', 'Да', ],
         ['<100', 'Средняя', 'Высокая', 'Да', 'Да', ],
         ['100-150', 'Средняя', 'Высокая', 'Нет', 'Да', ],
         ['100-150', 'Высокая', 'Средняя', 'Да', 'Да', ],
         ['>150', 'Средняя', 'Высокая', 'Нет', 'Нет', ],
         ]

X = ['<100', 'Средняя', 'Средняя', 'Да']
da = 0
net = 0
one = 0
two = 0
three = 0
four = 0
one1 = 0
two1 = 0
three1 = 0
four1 = 0
for i in table:
    if i[4] == 'Да':
        da += 1
    else:
        net += 1

Pc = net / len(table)
print('P(C2) =', Pc)
for i in table:
    if i[4] == 'Да' and i[0] == X[0]:
        one += 1
    if i[4] == 'Да' and i[1] == X[1]:
        two += 1
    if i[4] == 'Да' and i[2] == X[2]:
        three += 1
    if i[4] == 'Да' and i[3] == X[3]:
        four += 1
    if i[4] == 'Нет' and i[0] == X[0]:
        one1 += 1
    if i[4] == 'Нет' and i[1] == X[1]:
        two1 += 1
    if i[4] == 'Нет' and i[2] == X[2]:
        three1 += 1
    if i[4] == 'Нет' and i[3] == X[3]:
        four1 += 1
print('Да:', da, 'Нет:', net)
print(one / da, two / da, three / da, four / da, one1 / net, two1 / net, three1 / net, four1 / net, sep='\n')
print()
a = (one / da) * (two / da) * (three / da) * (four / da)
a1 = (one1 / net) * (two1 / net) * (three1 / net) * (four1 / net)
print(a, a1)
b = a * (da / len(table))
b1 = a1 * (net / len(table))
print(b, b1)
c = b / (b + b1)
c1 = b1 / (b + b1)
print()
print(c, c1)
