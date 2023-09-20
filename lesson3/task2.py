# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = 5
if a == 0:
    print(0)
else:
    f_p, f_n = 0, 1
    n = 2
    while f_n <= a:
        if f_n == a:
            print(n)
            break
        f_p, f_n = f_n, f_n + f_p
        n += 1
    else:
        print(-1)



