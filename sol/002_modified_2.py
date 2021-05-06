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
#  002.pyの高速化案として、bitをカッコ列に直す作業をfor文やif文を使わずに実装することを考えます。
#  Pythonの便利な関数replace()を用いて、stringのbitを直接カッコ列に直すことを考えます。
#  関数bin()を使うと"0b1001"のように ”0b” + bit の形で10進数を2進数に直すことができます。
#  しかしこのままでは ”0001" のような、0始まりのbitを作ることができないので、
#  N+1桁目が１になるようなbitを作り、”0b1" 以降をスライスすることでN桁のbitを生成します。
#  よって、for文のrangeは2**Nから2**(N+1)となります。
#  無事に高速化できました。002.pyの4-5倍ほど速く、002_modified_1.pyの2倍くらい速く実行できました。
for i in range(1<<N, 1<<(N+1)):
    brackets = bin(i)[3:]
    brackets = brackets.replace("0", "(")
    brackets = brackets.replace("1", ")")
    I = hantei(brackets)
    if I:
        print(brackets)