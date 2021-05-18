def find(r,c):
    if root[r*W+c] == -1:
        return (r,c)
    else:
        root[r*W+c] = find(*root[r*W+c])
        return root[r*W+c]

def same(ra,ca,rb,cb):
    return find(ra,ca) == find(rb,cb)

def unite(ra,ca,rb,cb):
    (ra,ca) = find(ra,ca)
    (rb,cb) = find(rb,cb)
    if (ra,ca) == (rb,cb):
        return
    root[ra*W+ca] = (rb,cb)

def get_nex(field, x, y):
    # マス(x,y)の四方にある赤いマスのリストを返す
    nex = []
    now = field[x][y]
    if field[x+1][y] == 1:
        nex.append((x+1, y))
    if field[x-1][y] == 1:
        nex.append((x-1, y))
    if field[x][y+1] == 1:
        nex.append((x, y+1))
    if field[x][y-1] == 1:
        nex.append((x, y-1))
    return nex


H, W = map(int, input().split())
field = [[0]*(W+2) for _ in range(H+2)]
root = [-1]*(W+1)*(H+1)

Q = int(input())
for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        r, c = query[1:]
        field[r][c] = 1
        for rb, cb in get_nex(field, r, c):
            unite(r, c, rb, cb)
    else:
        ra, ca, rb, cb = query[1:]
        if (field[ra][ca] == 1)and(field[rb][cb] == 1)and(same(ra,ca,rb,cb)):
            print("Yes")
        else:
            print("No")