N, K = map(int, input().split())
A = list(map(int, input().split()))
sA = sorted(A)
nA = [0] * N

for i in range(K):
    tmp = A[i::K]
    tmp.sort()
    for j in range(len(tmp)):
        nA[j * K + i] = tmp[j]
if sA == nA:
    print('Yes')
else:
    print('No')
