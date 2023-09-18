"""
                            Задача №67.
1. Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)

Чтобы подключить датасет с
пингвинами, воспользуйтесь данным
скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()
"""

# Вариант 1
import random
import seaborn as sns

penguins = sns.load_dataset("penguins")


def f(row):
    val = ''
    res = random.randint(1, 60)

    if res < 35:
        val = 'low'
    elif 35 < res < 42:
        val = 'middle'
    elif res > 42:
        val = 'high'

    return val



penguins['len'] = penguins.apply(f, axis=1)


print(penguins)



# Вариант 2
# import seaborn as sns

# # Загрузка датасета
# penguins = sns.load_dataset("penguins")
# penguins.head()

# # Функция для определения категории длины клюва
# def get_bill_length_category(length):
#     if length >= 42:
#         return "high"
#     elif 35 <= length < 42:
#         return "middle"
#     else:
#         return "low"

# # Применение функции к столбцу "bill_length_mm" и создание нового столбца "bill_length_category"
# penguins["bill_length_category"] = penguins["bill_length_mm"].apply(get_bill_length_category)

# # penguins.head()
# # Вывод первых 5 строк таблицы с пингвинами
# print(penguins.head())



