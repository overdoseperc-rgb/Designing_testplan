import math

def is_even(number):
    if type(number) is not int:
        raise TypeError("Ожидается целое число")
    return number % 2 == 0

def _dimension(value):
    if type(value) not in (int, float):
        raise TypeError("Ожидается число")
    if not math.isfinite(value) or value < 0:
        raise ValueError("Размер должен быть конечным и неотрицательным")

def calculate_area(length, width):
    _dimension(length)
    _dimension(width)
    return length * width

def classify_triangle(a, b, c):
    for side in (a, b, c):
        _dimension(side)
        if side == 0:
            raise ValueError("Стороны должны быть положительными")
    x, y, z = sorted((a, b, c))
    if x + y <= z:
        raise ValueError("Треугольник не существует")
    if a == b == c:
        return "равносторонний"
    if a == b or a == c or b == c:
        return "равнобедренный"
    return "разносторонний"
