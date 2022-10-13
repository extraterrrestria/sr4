import random
a = int(input('Введите размерность массива: '))
lst = []
for i in range(a):
    lst.append(random.randint(0, 30))
b = min(lst)
delta = int(input('Введите значение delta: '))
counter = 0
for i in lst:
    if i - delta == b:
        counter += 1
print(counter)
