import heapq

N, K = map(int, input().split())
queries = []
for _ in range(N):
    t, y = map(int, input().split())
    queries.append((t, y))

queries.reverse()
ans = -10 ** 15
cur = 0
q = []
heapq.heapify(q)
for t, y in queries:
    if t == 1:
        ans = max(ans, y + cur)
        if K == 0:
            K -= 1
            break
        K -= 1
        if len(q) > K:
            cur -= heapq.heappop(q)
    else:
        if y >= 0:
            cur += y
        else:
            heapq.heappush(q, -y)
            if len(q) > K:
                cur -= heapq.heappop(q)

if K >= 0:
    ans = max(ans, cur)
print(ans)
