"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3
Вывод:
2
"""

mas = [1, 2, 3, 2, 3, 3, 2]
count = 0
mas2 = []

for i in range(len(mas)):
    k = 1

    for j in range(i + 1, len(mas)):

        if mas[i] == mas[j] and mas[i] not in mas2:
            k += 1
            if k == 2:
                count += 1
                mas2.append(mas[i])
print(count)