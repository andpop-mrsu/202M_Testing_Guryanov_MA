import pytest
from triangle_class import Triangle, IncorrectTriangleSides

def test_triangle_creation():
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == 'nonequilateral'
    assert triangle.perimeter() == 12

def test_invalid_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 3)

def test_negative_sides():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-3, 4, 5)

def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)

def test_equilateral():
    triangle = Triangle(5, 5, 5)
    assert triangle.triangle_type() == 'equilateral'
    assert triangle.perimeter() == 15

def test_isosceles():
    triangle = Triangle(5, 5, 8)
    assert triangle.triangle_type() == 'isosceles'
    assert triangle.perimeter() == 18
