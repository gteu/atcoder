import heapq

n, m = map(int, input().split())
left = [set() for _ in range(n + 1)]
right = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if b in left[a]:
        print(-1)
        exit() 
    left[b].add(a)
    right[a].add(b)

ans = []
q = []
for i in range(1, n + 1):
    if len(left[i]) == 0:
        q.append(i)
heapq.heapify(q)

for _ in range(n):
    i = heapq.heappop(q)
    ans.append(i)
    for v in right[i]:
        left[v].remove(i)
        if len(left[v]) == 0:
            heapq.heappush(q, v)
print(*ans)