import matplotlib.pyplot as plt
import numpy as np
import math
  
x = np.linspace(-5, 25, 60)
z = 1/(1 + np.exp(-x))

weights = []
table = []
tab = []
for i in range(50):
  table.append([np.random.uniform(0, 10), 0])
  tab.append([np.random.uniform(15, 25), 1])
table = table + tab

for i in range(100):
  rand_start = np.random.rand(1, 2)
  weights.append(rand_start)
 # print('Начальные значения весов ', rand_start)
rand_dot = np.random.uniform(len(table))
#print('одной случайной точки', table[int(rand_dot)])
for i in range(100):
  logit = table[i][0] * rand_start[0][0] + table[i][1] * rand_start[0][1]
  sigmoid = 1/(1 + np.exp(-logit))
 # print(sigmoid)
  # if sigmoid > 0.5:
  #   print(sigmoid, '> 0.5')
  # else:
  #   print(sigmoid, '< 0.5')
  grad = [-1 * (table[i][0] * (1 - sigmoid)), -1 * (table[i][1] * (1 - sigmoid))]
  # print('градиентного спуска', grad)
  w = [rand_start[0][0] - grad[0], rand_start[0][1] - grad[1]]
  logloss = (w[1] * np.log1p(w[1]) + (1 - w[0]) * np.log1p(1 - w[1]))
  print(i, 'вес =', w, 'logloss =', logloss)
  weights[i] = w
  w = []
plt.plot(x, z)
plt.plot(*zip(*table), marker='o', color='r', ls='')
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")
  
plt.show()
