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
#  想定ソースコードを愚直にPythonで実装するとTLEするので高速化を図ります。
#  想定ソースコードのアルゴリズムでは、2**N通りのカッコ列を全探索していますが、
#  ")"から始まるカッコ列は必ず”正しくない”ので、bitで言えばN桁目が１になるような
#  bitは探索しなくて良いことがわかり、2**(N-1)までfor分を回せば良いことがわかります。
#  もう少し厳密に考えると、下限は "01", "0011", "000111", のように0と１がN/2個ずつ
#  並んだbitであることがわかり、上限は "01010...0101"と0と１が交互に並んだbitであることもわかります。
#  これらの数で探索範囲を見事半分以上絞ることができました。
#  なお、これでもまだTLEするので次の高速化案を考えることにします。002_modified_2.pyに示します。
start = 2**(N//2) - 1
end = sum([1<<(N-2*n) for n in range(1,N//2+1)]) + 1
for i in range(start, end):
    candidate = ""
    for j in range(N-1, -1, -1):
        if (i & (1<<j)) == 0:
            candidate += "("
        else:
            candidate += ")"
    I = hantei(candidate)
    if I:
        print(candidate)