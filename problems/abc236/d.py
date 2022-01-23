N = int(input())
A = []

for _ in range(2 * N - 1):
    A.append(list(map(int, input().split())))

ans = 0

used = [False] * (2 * N)

def dfs(i, s):
    if i == N:
        global ans
        ans = max(ans, s)
        return 
    
    for j in range(2 * N):
        if not used[j]:
            used[j] = True
            break
    
    for k in range(2 * N):
        if not used[k]:
            used[k] = True
            x = min(j, k)
            y = max(j, k)
            dfs(i + 1, s ^ A[x][y - x - 1])
            used[k] = False

    used[j] = False

dfs(0, 0)
print(ans)