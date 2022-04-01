N, M = map(int, input().split())
cond = []
for _ in range(M):
    A, B = map(int, input().split())
    cond.append((A - 1, B - 1))


K = int(input())
choice = []
for _ in range(K):
    C, D = map(int, input().split())
    choice.append((C - 1, D - 1))

ans = 0
for i in range(2 ** K):
    ball = [False] * N
    for j in range(K):
        if i >> j & 1:
            ball[choice[j][0]] = True
        else:
            ball[choice[j][1]] = True
    tmp = 0
    for a, b in cond:
        if ball[a] and ball[b]:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
