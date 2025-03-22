class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Sides must be positive")

        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides("The sides do not form a valid triangle")

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self) -> str:
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self) -> float:
        return self.a + self.b + self.c
