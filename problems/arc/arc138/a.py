N, K = map(int, input().split())
A = list(map(int, input().split()))

if min(A[:K]) >= max(A[K:]):
    print(-1)
    exit()

nA = []
for i, a in enumerate(A):
    nA.append((a, -i))
nA.sort()

lmax = -1
ans = N - 1
for a, i in nA:
    i *= -1
    if i < K:
        if i > lmax:
            lmax = i
    else:
        if lmax != -1:
            ans = min(ans, i - lmax)
print(ans)
