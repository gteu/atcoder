N = int(input())

T = []
L = []
for _ in range(N):
    A, B = map(int, input().split())
    T.append(A / B)
    L.append((A, B))

ls = 0
rs = sum(T)
d = 0
for i in range(N):
    ls += T[i]
    rs -= T[i]
    if ls >= rs:
        ls -= T[i]
        s = (rs - ls) * L[i][1]
        if s > 0:
            print(d + s + (L[i][0] - s) / 2)
        else:
            print(d + (L[i][0] + s) / 2)
        exit()
    d += L[i][0]
