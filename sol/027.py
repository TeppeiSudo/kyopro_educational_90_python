N = int(input())
names = set()

for n in range(1, N+1):
    s = str(input())
    if s not in names:
        names.add(s)
        print(n)