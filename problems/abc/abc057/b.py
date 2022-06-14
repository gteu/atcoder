N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(tuple(map(int, input().split())))
for _ in range(M):
    B.append(tuple(map(int, input().split())))
ans = []
for a, b in A:
    tmp = 10 ** 10
    tmp_i = -1
    for i, (c, d) in enumerate(B):
        if abs(a - c) + abs(b - d) < tmp:
            tmp = abs(a - c) + abs(b - d)
            tmp_i = i + 1
    ans.append(tmp_i)
print(*ans, sep='\n')
