# 二分探索を普通に再帰で実装

M = 2

ret = []

def dfs(a):
    if len(a) == 10:
        ret.append(a)
        return 

    for i in range(M):
        # dfs(a + str(i)) # <- ここが少し遅いらしい
        dfs("".join([a, str(i)])) # こうすればいいんじゃね

dfs("")

print(*ret, sep="\n")