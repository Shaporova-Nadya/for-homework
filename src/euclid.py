def gcd(a,b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = gcd(b, a % b)
        x = y1
        y = x1 - y1 * (a//b)
        return g, x, y

a = int(input())
b = int(input())
g, x, y = gcd(a,b)
print(f"НОД {a} и {b} равен {g}")
print(f"x равен {x}, y равен {y}")
print(f"Разложение Безу : {a}*{x} + {b}*{y} = {g}")


