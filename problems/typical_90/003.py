N = int(input())
to = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    to[A].append(B)
    to[B].append(A)

INF = 10 ** 9
stack = [0]
d = [INF] * N
d[0] = 0
while stack:
    cur = stack.pop()
    for nxt in to[cur]:
        if d[nxt] == INF:
            d[nxt] = d[cur] + 1
            stack.append(nxt)

i = d.index(max(d))
stack = [i]
d = [INF] * N
d[i] = 0
while stack:
    cur = stack.pop()
    for nxt in to[cur]:
        if d[nxt] == INF:
            d[nxt] = d[cur] + 1
            stack.append(nxt)
print(max(d) + 1)
