from itertools import product

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

def mod46_counter(X):
    Xmod = [0]*46
    for x in X:
        Xmod[x%46] += 1
    return Xmod

Amod = mod46_counter(A)
Bmod = mod46_counter(B)
Cmod = mod46_counter(C)

l = list(range(46))
ans = 0
for t in product(l, repeat=3):
    if sum(t)%46 == 0:
        ans += Amod[t[0]] * Bmod[t[1]] * Cmod[t[2]]
print(ans)