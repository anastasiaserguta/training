num = float(input())

print(int(num) % 3 == 0)

num = float(input())

print((num - int(num)) * 100 > 50)

a, b = map(int, input().split())

print(a % b == 0)

a, b, c = map(int, input().split())

print(a + b > c and a + c > b and b + c > a)

num = float(input())

print(0 <= num <= 2 or 10 <= num <= 20)