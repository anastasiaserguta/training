class TriangleChecker:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> int:
        if not all([type(x) in (int, float) and x > 0 for x in [self.a, self.b, self.c]]):
            return 1
        
        a, b, c = self.a, self.b, self.c
        if a + b < c or a + c < b or c + b < a:
            return 2
        
        return 3



a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

tr2 = TriangleChecker('4', 4.0, 5.0)
print(tr2.is_triangle())