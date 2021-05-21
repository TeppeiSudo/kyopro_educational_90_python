from math import gcd

a, b = map(int, input().split())
threshold = 10**18

c = a // gcd(a, b)
if b <= threshold // c:
    print(int(c*b))
else:
    print("Large")