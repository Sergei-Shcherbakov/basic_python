# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
element1 = []
element2 =[]
for i in range(n):
    element1.append(int(input(f'Введите {i + 1} элемент первого множества: ')))
for i in range(m):
    element2.append(int(input(f'Введите {i + 1} элемент второго множества: ')))

element1 = set(element1)
element2 = set(element2)
element3 = element1.union(element2)
element3 = list(element3)
element3.sort()
print(element3)