### Задача 1: Гибкий калькулятор
# Создайте функцию calculator, которая принимает два обязательных аргумента a и b,
# а также именованный аргумент operation со значением по умолчанию '+'.
# Поддерживаются операции: +, -, *, /, **
# Если операция не поддерживается, вернуть строку: "Операция {operation} не поддерживается!"
#
# Примеры:
# calculator(5, 3) → 8
# calculator(5, 3, operation='*') → 15
# calculator(10, 2, operation='/') → 5.0
# calculator(2, 3, operation='**') → 8
# calculator(2, 3, operation='%') → "Операция % не поддерживается!"

def calculator(a, b, operation='+'):
    pass

# Тесты
assert calculator(5, 3) == 8
assert calculator(5, 3, operation='*') == 15
assert calculator(10, 2, operation='/') == 5.0
assert calculator(2, 3, operation='**') == 8
assert calculator(2, 3, operation='%') == "Операция % не поддерживается!"
