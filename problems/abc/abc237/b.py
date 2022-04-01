h, w = map(int, input().split())

B = [[0] * h for _ in range(w)]

for i in range(h):
    V = list(map(int, input().split()))
    for j in range(w):
        B[j][i] = V[j]

for b in B:
    print(*b)