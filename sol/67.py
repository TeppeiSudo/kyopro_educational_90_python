N, K = map(int, input().split())

def solve(n):
    sN = str(n)
    num = 0
    for i, n in enumerate(reversed(sN)):
        num += int(n)*(8**i)

    if num == 0:
        nano = "0"
    else:
        nano = ""
        while num > 0:
            nano = str(num%9) + nano
            num //= 9

    res = ""
    for s in nano:
        if s == "8":
            res += "5"
        else:
            res += s
    return res

ans = N
for k in range(K):
    ans = solve(ans)
print(ans)