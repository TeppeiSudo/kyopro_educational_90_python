H, W = map(int, input().split())
A = [[0]*W]*H
Row = [0]*H
Column = [0]*W
Answer = [[0]*W for _ in range(H)]

# Step #1. 入力
for i in range(H):
    A[i] = list(map(int, input().split()))

# Step #2. 前計算
for i in range(H):
    for j in range(W):
        Row[i] += A[i][j]
        Column[j] += A[i][j]

# Step #3. 答えの計算
for i in range(H):
    for j in range(W):
        Answer[i][j] = Row[i] + Column[j] - A[i][j]

# Step #4. 出力
for i in range(H):
    print(*Answer[i])