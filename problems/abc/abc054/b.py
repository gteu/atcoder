N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(input())

for _ in range(M):
    B.append(input())

for i in range(N - M + 1):
    for j in range(N - M + 1):
        flag = True
        for x in range(M):
            for y in range(M):
                if A[i + x][j + y] != B[x][y]:
                    flag = False
        if flag:
            print('Yes')
            exit()
print('No')
