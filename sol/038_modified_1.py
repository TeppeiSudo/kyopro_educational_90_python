from math import gcd

def lcm(x, y):
    g = gcd(x, y)
    return int(x//g*y)

a, b = map(int, input().split())
l = lcm(a, b)

if l > 10**18:
    print("Large")
else:
    print(l)