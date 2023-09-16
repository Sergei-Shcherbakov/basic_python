# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
#
# Пример:
#
#
# n = 385916 -> yes
# n = 123456 -> no
n = 123456
res1 = n // 100000 + n % 100000 // 10000 + n % 100000 % 10000 // 1000
res2 = n % 100000 % 10000 % 1000 // 100 + n % 100000 % 10000 % 1000 % 100 // 10 + n % 100000 % 10000 % 1000 % 100 % 10
if res1 == res2:
    print('yes')
else:
    print('no')