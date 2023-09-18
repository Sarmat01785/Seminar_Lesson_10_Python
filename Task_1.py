"""
                                    Задача №63.
1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age
"""


# Вариант 1
# import pandas as pd
# import matplotlib.pyplot as plt

# # Загрузка данных из файла
# data = pd.read_csv('california_housing_test.csv')

# # 1. Точечный график households к population
# plt.scatter(data['households'], data['population'])
# plt.xlabel('Households')
# plt.ylabel('Population')
# plt.title('Households vs Population')
# plt.show()

# # 2. Линейный график longitude по отношению к median_house_value
# plt.plot(data['longitude'], data['median_house_value'])
# plt.xlabel('Longitude')
# plt.ylabel('Median House Value')
# plt.title('Longitude vs Median House Value')
# plt.show()

# # 3. Гистограмма по housing_median_age
# plt.hist(data['housing_median_age'])
# plt.xlabel('Housing Median Age')
# plt.ylabel('Frequency')
# plt.title('Housing Median Age Histogram')
# plt.show()

# # 4. Гистограмма по median_house_value с оттенком housing_median_age
# plt.hist2d(data['median_house_value'], data['housing_median_age'])
# plt.xlabel('Median House Value')
# plt.ylabel('Housing Median Age')
# plt.title('Median House Value Histogram with Housing Median Age')
# plt.colorbar()
# plt.show()



# Вариант 2
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('california_housing_test.csv')


# 1
def first(data):
    households = list(data.households)
    population = list(data.population)

    plt.scatter(households, population)

    plt.xlabel("households")
    plt.ylabel("population")

    plt.title("Scatter plot for households and population")
    plt.show()


# first()

# 2
def second(data):
    longitude = list(data.longitude)
    median_house_value = list(data.median_house_value)

    plt.plot(longitude, median_house_value)

    plt.xlabel("longitude")
    plt.ylabel("median_house_value")

    plt.title("Line plot for longitude and median_house_value")

    plt.show()


# Гистограммы агрегируют числовые данные по группам с равными интервалами,
# которые называют бинами, и отображают частоту
# встречаемости значений в каждом из бинов
# second()
def third():
    housing_median_age = list(data.housing_median_age)

    plt.hist(housing_median_age, bins=7, edgecolor='black')

    plt.title("Hist plot for housing_median_age")

    plt.show()


# third()


# fourth
def fourth():
    median_house_value = list(data.median_house_value)
    housing_median_age = list(data.housing_median_age)

    plt.hist(housing_median_age, bins=7, edgecolor='black')
    plt.hist(median_house_value, bins=7)

    plt.show()


# fourth()

# Вызов функций
first(data)
second(data)
third()
fourth()

