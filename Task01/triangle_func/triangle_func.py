class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a: float, b: float, c: float) -> str:
    """
    Определяет тип треугольника по длинам его сторон.

    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(5, 5, 5)
    'equilateral'
    >>> get_triangle_type(5, 5, 8)
    'isosceles'
    >>> get_triangle_type(1, 1, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: The sides do not form a valid triangle
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Sides must be positive")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("The sides do not form a valid triangle")

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"
