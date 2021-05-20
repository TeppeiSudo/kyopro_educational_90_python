a, b, c = map(int, input().split())
e = 1

for _ in range(b):
    e *= c
if a < e:
    print("Yes")
else:
    print("No")