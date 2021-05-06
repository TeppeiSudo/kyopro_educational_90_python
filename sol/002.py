def hantei(S):
    dep = 0
    for s in S:
        if s == "(":
            dep += 1
        elif s == ")":
            dep += -1
        if dep < 0:
            return False
    if dep == 0:
        return True
    else:
        return False


N = int(input())
for i in range(1<<N):
    candidate = ""
    for j in range(N-1, -1, -1):
        # メモ: (i & (1<<j)) = 0 というのは、i の j ビット目（2^j の位）が 0 であるための条件。
        #       頻出なので知っておくようにしましょう。
        if (i & (1<<j)) == 0:
            candidate += "("
        else:
            candidate += ")"
    I = hantei(candidate)
    if I:
        print(candidate)