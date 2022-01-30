N, Q = map(int, input().split())
to = [[-1, -1] for _ in range(N)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] <= 2:
        x, y = q[1], q[2]
        x -= 1
        y -= 1
        if q[0] == 1:
            to[x][1] = y
            to[y][0] = x
        else:
            to[x][1] = -1
            to[y][0] = -1
            
    else:
        ans = []
        cur = q[1] - 1
        while to[cur][0] != -1:
            cur = to[cur][0]
        while to[cur][1] != -1:
            ans.append(cur + 1)
            cur = to[cur][1]
        ans.append(cur + 1)
        print(len(ans), *ans)