# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint


n = int(input('Введите число:'))
A = B = 0

for i in range(n):
    side = randint(0,1)
    if side < 1:
        A += 1
    elif side > 0:
        B += 1
    print(side)


if A < B:
    print(f'Монет на стороне решка = {A}')
elif A > B:
    print(f'Монет на стороне герба = {B}')



