### Задача 5: Сумма последовательностей
# Функция sum_sequences принимает любое количество списков чисел (*args)
# Возвращает список с суммами каждого списка.
#
# Примеры:
# sum_sequences([1, 2, 3], [4, 5], [10, -10, 10]) → [6, 9, 10]
# sum_sequences([], [100], []) → [0, 100, 0]

def sum_sequences(*args):
    pass

# Тесты
assert sum_sequences([1, 2, 3], [4, 5], [10, -10, 10]) == [6, 9, 10]
assert sum_sequences([], [100], []) == [0, 100, 0]
