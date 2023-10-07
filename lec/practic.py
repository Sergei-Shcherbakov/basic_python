lst = [1, 2, 3, 5, 8, 15, 23, 38]
lst1 = []
def f(lst, lst1):
    for el in lst:
        if el % 2 == 0:
            lst1.append((el, el**2))
    return lst1

print(f(lst, lst1))
