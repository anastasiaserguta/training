from math import sqrt, pow

a, b = map(int, input().split())

print(round(sqrt(pow(a, 2) + pow(b, 2)), 2))