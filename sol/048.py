N, K = map(int, input().split())

scores = []
for _ in range(N):
    a, b = map(int, input().split())
    scores.append(b)
    scores.append(a-b)

ans = 0
scores.sort(reverse=True)
for i in range(K):
    ans += scores[i]

print(ans)