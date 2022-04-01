from bisect import bisect_right
N, K = map(int, input().split())
P = []
for _ in range(N):
    P.append(sum(map(int, input().split())))
sorted_P = sorted(P)

for p in P:
    if bisect_right(sorted_P, p + 300) > N - K:
        print('Yes')
    else:
        print('No')
