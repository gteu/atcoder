import bisect

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

S = [[] for _ in range(N+1)]
for qi, q in enumerate(Q):
    for i in range(1,int(pow(q,0.5))+1):
        if q % i == 0:
            S[i].append(qi)
            if i != q//i:
                S[q//i].append(qi)

LIS = [10 ** 18] * N
for p in P:
    if len(S[p]) > 0:
        for s in reversed(S[p]):
            LIS[bisect.bisect_left(LIS, s)] = s
print(bisect.bisect_left(LIS, 10 ** 18))