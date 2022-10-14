import random
size = int(input('Введите размерность массива: '))
lst = []
for i in range(size):
    lst.append(random.randint(0, 30))
minim = lst[0]
for j in range(1, size):
    if lst[j] < minim:
        minim = lst[j]
delta = int(input('Введите значение delta: '))
counter = 0
for k in range(size):
    if lst[k] - delta == minim:
        counter += 1
print(counter)