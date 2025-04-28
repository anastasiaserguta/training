class TriangleChecker:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> int:
        if not isinstance(self.a, int | float) and not isinstance(self.b, int | float) and not isinstance(self.c, int | float):
            return 1
        elif a + b < c or a + c < b or c + b < a:
            return 2
        else:
            return 3



a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

tr2 = TriangleChecker('4', 4.0, 5.0)
print(tr2.is_triangle())