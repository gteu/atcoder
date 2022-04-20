import sys
input = sys.stdin.readline
N = int(input())
edges = []
to = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
    edges.append((a, b))

dist = [-1] * N
dist[0] = 0
stack = [0]
while stack:
    cur = stack.pop()
    for nxt in to[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            stack.append(nxt)

Q = int(input())
points = [0] * N
for _ in range(Q):
    t, e, x = map(int, input().split())
    e -= 1
    if t == 1:
        a, b = edges[e]
    else:
        b, a = edges[e]
    if dist[a] < dist[b]:
        points[0] += x
        points[b] -= x
    else:
        points[a] += x

stack = [(0)]
while stack:
    cur = stack.pop()
    for nxt in to[cur]:
        if dist[cur] < dist[nxt]:
            stack.append(nxt)
            points[nxt] += points[cur]
print(*points, sep='\n')
