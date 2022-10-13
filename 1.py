size = int(input('Введите размерность массива: '))
arr = []
for i in range(size):
    arr.append(float(input('Введите элементы массива: ')))
maxim = arr[0]
index = 0
for j in range(1, size):
    if arr[j] > maxim:
        maxim = arr[j]
        index = j + 1
for k in  range(index, size):
    arr[k] = 0
print(*arr)

