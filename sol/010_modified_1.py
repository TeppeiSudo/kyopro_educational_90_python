N = int(input())
C1 = [0]*N
C2 = [0]*N
sumC1 = [0]*(N+1)
sumC2 = [0]*(N+1)

for n in range(N):
    c, p = map(int, input().split())
    if c == 1:
        C1[n] = p
    else:
        C2[n] = p
    # 累積和を取る
    sumC1[n+1] = sumC1[n] + C1[n]
    sumC2[n+1] = sumC2[n] + C2[n]

# クエリに答える
Q = int(input())
for q in range(Q):
    l, r = map(int, input().split())
    ans1 = sumC1[r]-sumC1[l-1]
    ans2 = sumC2[r]-sumC2[l-1]
    print(ans1, ans2)