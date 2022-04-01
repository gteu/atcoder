N, M = map(int, input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    to[A].append(B)
    to[B].append(A)

visited = [False] * N
for i in range(N):
    if not visited[i]:
        s = []
        s.append((-1, i))
        visited[i] = True
        while s:
            pre, cur = s.pop()
            for nxt in to[cur]:
                if not visited[nxt]:
                    s.append((cur, nxt))
                    visited[nxt] = True
                elif nxt != pre:
                    print('No')
                    exit()

for i in range(N):
    if len(to[i]) > 2:
        print('No')
        exit()
print('Yes')
