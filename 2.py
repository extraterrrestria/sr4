import random
a = int(input('Введите размерность массива 1: '))
b = int(input('Введите размерность массива 2: '))
lsta = []
lstb = []
for i in range(a):
    lsta.append(random.randint(0, 30))
for j in range(b):
    lstb.append(random.randint(0, 30))
for k in set(lstb):
    if k in lsta:
        print(k)