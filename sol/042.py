K = int(input())

if K % 9 == 0:
    dp = [0]*(K+1)
    dp[0] = 1
    for i in range(1, K+1):
        dp[i] = sum([dp[i-n] for n in range(1, min(i,9)+1)])
        dp[i] %= 1000000007
    print(dp[K])
else:
    print(0)