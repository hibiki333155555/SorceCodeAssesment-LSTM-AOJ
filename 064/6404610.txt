def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


x, y = map(int, input().split())
print(gcd(x, y))
