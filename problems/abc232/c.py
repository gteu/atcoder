import itertools

N, M = map(int, input().split())
A, B = [[False] * N for _ in range(N)], [[False] * N for _ in range(N)]
for i in range(M):
    tmp1, tmp2 = map(int, input().split())
    tmp1 -= 1
    tmp2 -= 1
    A[tmp1][tmp2], A[tmp2][tmp1] = True, True
for i in range(M):
    tmp1, tmp2 = map(int, input().split())
    tmp1 -= 1
    tmp2 -= 1
    B[tmp1][tmp2], B[tmp2][tmp1] = True, True

for p in itertools.permutations(range(N)):
    is_same = True
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[p[i]][p[j]]:
                is_same = False
                break
    if is_same:
        print("Yes")
        exit()
print("No")