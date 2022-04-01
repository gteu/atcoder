N, M = map(int, input().split())
P = []
top = [[] for _ in range(N)]
q = []
for i in range(M):
    _ = input()
    p = list(map(lambda x: int(x) - 1, input().split()))
    p.reverse()
    P.append(p)
    v = p[-1]
    top[v].append(i)
    if len(top[v]) == 2:
        q.append(v)

left_count = N
while q:
    v = q.pop()
    for i in top[v]:
        P[i].pop()
        if P[i]:
            nxt_v = P[i][-1]
            top[nxt_v].append(i)
            if len(top[nxt_v]) == 2:
                q.append(nxt_v)
    left_count -= 1

if left_count == 0:
    print("Yes")
else:
    print("No")