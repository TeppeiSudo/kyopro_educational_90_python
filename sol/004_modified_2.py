H, W = map(int, input().split())

# Step #1. 入力
A = [list(map(int, input().split())) for _ in range(H)]

# Step #2. 前計算
Row = [sum(row) for row in A]
Column = [sum(col) for col in zip(*A)]

# Step #3. 答えの計算
Answer = [[str(row+col-a) for col, a in zip(Column, A_row)] for row, A_row in zip(Row, A)]

# Step #4. 出力
# listの参照をすべて取り除くことでギリギリでAC
print("\n".join([" ".join(line) for line in Answer]))