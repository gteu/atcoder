from heapq import heappush, heappop

Q = int(input())
cur = 0
ball = []
ans = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        heappush(ball, x - cur)
    elif q[0] == 2:
        x = q[1]
        cur += x
    else:
        v = heappop(ball)
        ans.append(v + cur)

print(*ans, sep='\n')
