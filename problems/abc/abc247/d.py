from collections import deque
Q = int(input())
que = deque([])
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 1:
        x, c = q
        que.append((x, c))
    else:
        cnt = 0
        ans = 0
        while cnt < q[0]:
            x, c = que.popleft()
            cnt += c
            ans += c * x
        if cnt > q[0]:
            que.appendleft((x, cnt - q[0]))
            ans -= x * (cnt - q[0])
        print(ans)
