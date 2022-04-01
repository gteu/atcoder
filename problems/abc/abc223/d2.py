import heapq

n, m = map(int, input().split())
A = [[] for _ in range(n)]
d = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A[a].append(b)
    d[b] += 1

ans = []
q = []
for i in range(n):
    if d[i] == 0:
        q.append(i)
heapq.heapify(q)

for _ in range(n):
    if len(q) == 0:
        print(-1)
        exit()
    i = heapq.heappop(q)
    ans.append(i + 1)
    for v in A[i]:
        d[v] -= 1
        if d[v] == 0:
            heapq.heappush(q, v)
print(*ans)