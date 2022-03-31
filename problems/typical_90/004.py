H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

h_sum = [0] * H
w_sum = [0] * W
for i in range(H):
    for j in range(W):
        h_sum[i] += A[i][j]
        w_sum[j] += A[i][j]

for i in range(H):
    ret = []
    for j in range(W):
        ret.append(h_sum[i] + w_sum[j] - A[i][j])
    print(*ret)
