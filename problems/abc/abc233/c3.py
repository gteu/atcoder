N, X = map(int, input().split())
L = []
for i in range(N):
    line = list(map(int, input().split()))
    L.append(line[1:])

def dfs(i, v):
    if i == N:
        if v == X:
            return 1
        else:
            return 0

    else:
        ret = 0
        for j in range(len(L[i])):
            ret += dfs(i+1, v * L[i][j])
        return ret

print(dfs(0, 1))
