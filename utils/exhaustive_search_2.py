# 二分探索をリストをスタックみたいに用いて再帰で実装

M = 2

ret = []

def dfs(a):
    if len(a) == 5:
        ret.append("".join(a))
        return 

    for i in range(M):
        a.append(str(i))
        dfs(a)
        a.pop()

dfs([])

print(*ret, sep="\n")
