# Задача №69. Решение в группах
# 1. Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ

import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

sns.histplot(penguins, x='flipper_length_mm', hue='len')
plt.show()