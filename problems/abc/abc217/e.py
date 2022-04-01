from collections import deque
import heapq

Q = int(input())
que = deque()
sort_que = []
ans = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        que.append(q[1])
    elif q[0] == 2:
        if sort_que:
            ans.append(heapq.heappop(sort_que))
        else:
            ans.append(que.popleft())
    else:
        for q in que:
            heapq.heappush(sort_que, q)
        que = deque()
print(*ans, sep='\n')
