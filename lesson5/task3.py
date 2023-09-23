# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_prime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag

print(is_prime(9))

def is_prime_recur(n, flag, i):
    if i < n:
        if n % i == 0:
            flag = False
        return is_prime_recur(n, flag, i+1)
    return flag
print(is_prime_recur(5, flag=True, i=2))