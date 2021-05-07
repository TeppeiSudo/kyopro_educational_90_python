H, W = map(int, input().split())

# Step #1. 入力
A = [list(map(int, input().split())) for _ in range(H)]

# Step #2. 前計算
Row = [sum(row) for row in A]
Column = [sum(col) for col in zip(*A)]

# Step #3. 答えの計算
Answer = [[str(Row[h]+Column[w]-A[h][w]) for w in range(W)] for h in range(H)]

# Step #4. 出力
# 004.pyは当然TLEなので高速化を図る
# すべてのfor文を内包表記にしたが、TLE
print("\n".join([" ".join(Answer[h]) for h in range(H)]))