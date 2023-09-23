# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

mas = [0, 3, 3, 3, 4, 4]

num_min = min(mas)
num_max = max(mas)
res = []

for num in mas:
    if num == num_max:
        res.append(num_min)
    else:
        res.append(num)

print(res)


def func(mas, res=[], num_min=min(mas), num_max=max(mas)):
    if len(mas) == 0:
        return res

    if mas[0] == num_max:
        res.append(num_min)
    else:
        res.append(mas[0])

    return func(mas[1:], res, num_min, num_max)


print(func(mas))
def func(mas, res, num_min, num_max):
    if len(mas) == 0:
        return res

    if mas[0] == num_max:
        res.append(num_min)
    else:
        res.append(mas[0])

    return func(mas[1:], res, num_min, num_max)

mas = [0, 3, 3, 3, 4, 4]

print(func(mas, res=[], num_min=min(mas), num_max=max(mas)))