N = int(input())
to = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

for i in range(N):
    to[i].sort(reverse = True)

s = [0]
visited = [None] * N
visited[0] = 0
ans = []
while s:
    cur = s.pop()
    ans.append(cur + 1)

    is_next = False
    while to[cur]:
        nxt = to[cur].pop()
        if visited[nxt] is None:
            s.append(nxt)
            visited[nxt] = cur
            is_next = True
            break

    if not is_next:
        if cur == 0:
            break
        else:
            s.append(visited[cur])

print(*ans)
