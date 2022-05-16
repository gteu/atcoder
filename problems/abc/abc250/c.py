N, Q = map(int, input().split())
A = list(range(N))
toi = {i: i for i in range(N)}
for _ in range(Q):
    x = int(input()) - 1
    if toi[x] != N - 1:
        curi, nxti = toi[x], toi[x] + 1
    else:
        curi, nxti = toi[x], toi[x] - 1
    curv, nxtv = A[curi], A[nxti]
    A[curi] = nxtv
    A[nxti] = curv
    toi[curv] = nxti
    toi[nxtv] = curi
print(*list(map(lambda x: x + 1, A)))
