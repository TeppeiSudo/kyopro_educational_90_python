N, Q = map(int, input().split())
A = list(map(int, input().split()))

shift = 0
for _ in range(Q):
    t, x, y = list(map(int, input().split()))
    if t == 1:
        # Pythonではリストの参照に負の数を使える。
        # A[-i]は後ろから数えてi番目という意味。
        # ただし-0という書き方は存在しないため、-1が一番最後であることに注意。
        A[x-1-shift], A[y-1-shift] = A[y-1-shift], A[x-1-shift]
    elif t == 2:
        shift += 1
        shift %= N
    else:
        print(A[x-1-shift])