import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pref = [[] for _ in range(N + 1)]
for i in range(M):
    P, Y = map(int, input().split())
    pref[P].append((Y, i))

for i in range(N + 1):
    pref[i].sort()

ans = []
for i in range(N + 1):
    for j, (_, k) in enumerate(pref[i]):
        id = str(i).zfill(6) + str(j + 1).zfill(6)
        ans.append((k, id))
ans.sort()
for i in range(M):
    print(ans[i][1])
