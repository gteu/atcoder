import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = []
for _ in range(M):
    k, *s = map(int, input().split())
    S.append(s)
P = list(map(int, input().split()))

ans = 0
for i in range(2 ** N):
    light = [False] * N
    for j in range(N):
        if i >> j & 1:
            light[j] = True
    ok = True
    for j in range(M):
        if P[j] != sum([light[s - 1] for s in S[j]]) % 2:
            ok = False
    ans += ok
print(ans)
