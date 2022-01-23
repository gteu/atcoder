N = int(input())
T = []
A = []
for i in range(N):
    line = list(map(int, input().split()))
    T.append(line[0])
    A.append(list(map(lambda x: x-1, line[2:])))

stack = [N - 1]
visited = [False] * N
visited[N - 1] = True
ans = 0
while stack:
    v = stack.pop()
    ans += T[v]
    for nxt in A[v]:
        if not visited[nxt]:
            stack.append(nxt)
            visited[nxt] = True

print(ans)