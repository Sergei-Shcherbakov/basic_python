# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
#
# Пример:
#
#
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 10
res = 0
for i in range(len(list_1)):
    if k - list_1[i] == 1:
        res = list_1[i]
    elif k - list_1[i] == 0:
        res = list_1[i]
        break
    elif k - list_1[i] == -1:
        res = list_1[i]
print(res)