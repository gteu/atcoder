N = int(input())
A = []
for _ in range(N):
    A.append(input())

ans = 0
for i in range(N):
    for j in range(N):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                cur = ''
                if di == 0 and dj == 0:
                    continue
                ni, nj = i, j
                for _ in range(N):
                    cur += A[ni][nj]
                    ni = (ni + di) % N
                    nj = (nj + dj) % N
                ans = max(ans, int(cur))
print(ans)
