N = int(input())
A = []*N

ans = 1
for n in range(N):
    A = list(map(int, input().split()))
    ans *= sum(A)
    ans %= (10**9+7)

print(ans)