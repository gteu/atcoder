from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

Q = int(input())
ans_ = []
for _ in range(Q):
    x, k = map(int, input().split())
    ans = 0
    x -= 1
    visited = set([x])
    q = deque()
    q.append((x, 0))
    while q:
        cur, cnt = q.popleft()
        if cnt <= k:
            ans += cur + 1
        else:
            break
        for nxt in edges[cur]:
            if nxt not in visited:
                q.append((nxt, cnt + 1))
                visited.add(nxt)
    ans_.append(ans)
print(*ans_, sep='\n')
