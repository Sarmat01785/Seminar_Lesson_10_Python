"""
                            Задача №65.
Написать EDA для датасета про пингвинов
Необходимо:
1. Использовать 2-3 точечных графика
2. Применить доп измерение в точечных графиках, используя
аргументы hue
3. Использовать PairGrid с типом графика на ваш выбор
4. Изобразить Heatmap
5. Использовать 2-3 гистограммы

Чтобы подключить датасет с
пингвинами, воспользуйтесь данным
скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()
"""


# Вариант 1
# Seaborn — библиотека для создания
# статистических графиков на Python

# разведочный анализ данных (EDA) по заданному дата сету

import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins")


# Использовать 2-3 точечных графика
def f_1():
    plt.scatter(penguins['bill_length_mm'], penguins['bill_depth_mm'])
    plt.show()

    plt.scatter(penguins['flipper_length_mm'], penguins['body_mass_g'])
    plt.show()


# Применить доп измерение в точечных графиках, используя
# аргументы hue
# hue='sex' - разбивка по полу
# size=5 - размер точек
def f_2():
    sns.catplot(data=penguins, x='flipper_length_mm', y='body_mass_g',
                hue='sex',
                size=5)

    plt.show()


# Использовать PairGrid с типом графика на ваш выбор
# создадим объект класса PairGrid, в качестве данных передадим ему
# как количественные, так и категориальные переменные
def f_3():
    x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm",
              "flipper_length_mm"]
    y_vars = ["body_mass_g"]
    g = sns.PairGrid(penguins, hue="species", x_vars=x_vars, y_vars=y_vars)
    g.map_diag(sns.histplot, color=".3")
    g.map_offdiag(sns.scatterplot)
    g.add_legend()
    plt.show()


# Изобразить Heatmap
def f_4():
    sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")
    plt.show()


# Использовать 2-3 гистограммы
def f_5():
    penguins['bill_depth_mm'].hist(bins=4)
    plt.show()


# Вызов функций для отображения графиков
f_1()
f_2()
f_3()
f_4()
f_5()




# Вариант 2
# import matplotlib.pyplot as plt
# import seaborn as sns

# penguins = sns.load_dataset("penguins")

# # 1. Использовать 2-3 точечных графика
# def scatter_plots():
#     plt.scatter(penguins['bill_length_mm'], penguins['bill_depth_mm'])
#     plt.scatter(penguins['flipper_length_mm'], penguins['body_mass_g'])
#     plt.xlabel('Bill Length (mm)')
#     plt.ylabel('Bill Depth (mm)')
#     plt.show()

# # 2. Применить доп измерение в точечных графиках, используя аргумент hue
# def scatter_plot_with_hue():
#     sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species')
#     plt.xlabel('Flipper Length (mm)')
#     plt.ylabel('Body Mass (g)')
#     plt.show()

# # 3. Использовать PairGrid с типом графика на ваш выбор
# def pairgrid_plot():
#     x_vars = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
#     y_vars = ["body_mass_g"]
#     g = sns.PairGrid(penguins, x_vars=x_vars, y_vars=y_vars)
#     g.map_upper(sns.scatterplot)
#     g.map_lower(sns.kdeplot)
#     g.map_diag(sns.histplot)
#     g.add_legend()
#     plt.show()

# # 4. Изобразить Heatmap
# def heatmap():
#     plt.figure(figsize=(8, 6))
#     sns.heatmap(penguins.corr(), annot=True, cmap='coolwarm')
#     plt.title('Correlation Heatmap')
#     plt.show()

# # 5. Использовать 2-3 гистограммы
# def histograms():
#     fig, axes = plt.subplots(2, 1)
#     penguins['bill_depth_mm'].plot.hist(ax=axes[0], bins=20)
#     penguins['flipper_length_mm'].plot.hist(ax=axes[1], bins=20)
#     axes[0].set_xlabel('Bill Depth (mm)')
#     axes[0].set_ylabel('Count')
#     axes[1].set_xlabel('Flipper Length (mm)')
#     axes[1].set_ylabel('Count')
#     plt.tight_layout()
#     plt.show()

# scatter_plots()
# scatter_plot_with_hue()
# pairgrid_plot()
# heatmap()
# histograms()








