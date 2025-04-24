### Задача 4: Нормализация данных
# Функция normalize принимает *args и method='minmax'
# - minmax: x_norm = (x - min) / (max - min)
# - mean: x_norm = x / mean
# Возвращает список нормализованных значений.
#
# Примеры:
# normalize(1, 2, 3, 4, 5) → [0.0, 0.25, 0.5, 0.75, 1.0]
# normalize(2, 4, 6, method='mean') → [0.5, 1.0, 1.5]

def normalize(*args, method='minmax'):
    pass

# Тесты
assert normalize(1, 2, 3, 4, 5) == [0.0, 0.25, 0.5, 0.75, 1.0]
assert normalize(2, 4, 6, method='mean') == [0.5, 1.0, 1.5]
