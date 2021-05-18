class UnionFind:
    def __init__(self, sz):
        self.par = [-1]*sz

    def root(self, pos):
        if self.par[pos] == -1:
            return pos
        else:
            self.par[pos] = self.root(self.par[pos])
            return self.par[pos]
    
    def unite(self, u, v):
        u = self.root(u)
        v = self.root(v)
        if u == v:
            return
        else:
            self.par[u] = v

    def same(self, u, v):
        if self.root(u) == self.root(v):
            return True
        else:
            return False


def query1(px, py):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        sx = px + dx[i]
        sy = py + dy[i]
        if not used[sx][sy]:
            continue
        else:
            hash1 = (px-1)*W + (py-1)
            hash2 = (sx-1)*W + (sy-1)
            UF.unite(hash1, hash2)
    used[px][py] = True


def query2(px, py, qx, qy):
    if (not used[px][py]) or (not used[qx][qy]):
        return False
    else:
        hash1 = (px-1)*W + (py-1)
        hash2 = (qx-1)*W + (qy-1)
        if UF.same(hash1, hash2):
            return True
        else:
            return False


# Step #1. 入力
H, W = map(int, input().split())
Q = int(input())
used = [[False]*(W+2) for _ in range(H+2)]

# Step #2. Union Find の初期化
UF = UnionFind(H*W)

# Step #3. クエリ処理
for i in range(1, Q+1):
    input_line = list(map(int, input().split()))
    ty = input_line[0]
    if ty == 1:
        x, y = input_line[1:]
        query1(x, y)
    else:
        xa, xb, ya, yb = input_line[1:]
        Answer = query2(xa, xb, ya, yb)
        if Answer:
            print("Yes")
        else:
            print("No")