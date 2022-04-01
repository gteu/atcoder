from heapq import heappop, heappush, heapify

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = []
h = P[:K]
heapify(h)
ans.append(h[0])
for p in P[K:]:
    tmp = heappop(h)
    if p < tmp:
        heappush(h, tmp)
    else:
        heappush(h, p)
    ans.append(h[0])

print(*ans, sep='\n')