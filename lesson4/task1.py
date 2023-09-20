# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


input_string = "a a a b c a a d c d d"
result = [] # Массив
counts = {} # Словарь

# Разделить строку на отдельные символы
characters = input_string.split()

for char in characters:
  if char in counts: # Вхождение в массив
    result.append(f"{char}_{counts[char]}")
    counts[char] += 1
  else:
    counts[char] = 1
    result.append(char)
print(' '.join(result))