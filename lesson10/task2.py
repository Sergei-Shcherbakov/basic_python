"""
Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы

"""

import seaborn as sns
import matplotlib.pyplot as plt
penguins = sns.load_dataset('penguins')

def f_1():
    # plt.scatter(penguins['bill_length_mm'], penguins['bill_depth_mm'])
    # plt.show()
    plt.scatter(penguins['flipper_length_mm'], penguins['body_mass_g'])
    plt.show()
    sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g")
    plt.show()

# f_1()

def f_2():
    sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue='sex', size=5, style='island')
    plt.show()


# f_2()

def f_3():
    x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
    y_vars = ['sex']
    g = sns.PairGrid(penguins, x_vars=x_vars, y_vars=y_vars, hue='species')
    g.map(sns.scatterplot)
    plt.show()
#
# f_3()


def f_4():
    sns.displot(penguins, x='bill_length_mm', y='bill_depth_mm', hue='species')
    plt.show()


# f_4()

def f_5():
    penguins['bill_depth_mm'].hist(bins=10)
    plt.show()

f_5()