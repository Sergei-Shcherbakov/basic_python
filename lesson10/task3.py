"""
Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""


import seaborn as sns
import matplotlib.pyplot as plt
from random import randint
import csv

penguins = sns.load_dataset('penguins')

def f(row):
    res = randint(1,60)
    val = None
    if res < 35:
        val = 'low'
    elif 35 < res < 42:
        val = 'middle'
    elif res > 42:
        val = 'high'
    return val

penguins['len'] = penguins.apply(f, axis=1)
print(penguins)

penguins.to_csv('penguins.csv')

# sns.histplot(penguins, x='flipper_length_mm', hue='len')
# plt.show()
