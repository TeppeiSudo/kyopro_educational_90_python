N, L = map(int, input().split())

dp = [0]*(N+1)
dp[0] = 1
for n in range(1, N+1):
    dp[n] = dp[n-1]
    if n >= L:
        dp[n] += dp[n-L]

print(dp[N]%(10**9+7))