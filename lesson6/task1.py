# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки

n = 7
# lst1 = [int(input("Введите число: ")) for i in range(n)]
lst1 = [3, 1, 3, 4, 2, 4, 12]
print("Второй массив")
m = 6
# lst2 = [int(input("Введите число: ")) for i in range(m)]
lst2 = [4, 15, 43, 1, 15, 1]

#традиционный итератор с функцией апенд
mas = []
for item in lst1:
    if item not in lst2:
        mas.append(item)
print(mas)


mas2 = [item for item in lst1 if item not in lst2]
print(mas2)