import math

### Задача 2: Расширенная геометрия
# Функция geometry принимает figure и *args.
# - 'circle': один аргумент (радиус), возвращает площадь круга (πr^2)
# - 'rectangle': два аргумента (стороны), возвращает площадь прямоугольника
# - 'triangle': три аргумента (стороны), площадь по формуле Герона
# - иначе: вернуть "Фигура не поддерживается!"
#
# Примеры:
# geometry(figure='circle', *(3,)) → ~28.274
# geometry(figure='rectangle', *(4, 5)) → 20
# geometry(figure='triangle', *(3, 4, 5)) → 6.0
# geometry(figure='hexagon', *(2,2,2,2,2,2)) → "Фигура не поддерживается!"

def geometry(*args, figure):
    pass

# Тесты
assert geometry(3, figure='circle') == 3.14 * 3**2
assert geometry(4, 5, figure='rectangle') == 20
assert geometry(3, 4, 5, figure='triangle') == 6.0
assert geometry(2, 2, 2, 2, 2, 2, figure='hexagon') == "Фигура не поддерживается!"
