num = 1230

def reverse(num):
    if num < 10:
        return str(num)

    return str(num % 10) + reverse(num // 10)

print(reverse(num))