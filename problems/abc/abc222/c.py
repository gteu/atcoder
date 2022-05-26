N, M = map(int, input().split())
A = []
scores = [[0, i] for i in range(2 * N)]
for _ in range(2 * N):
    A.append(input())

for i in range(M):
    scores.sort(key=lambda x: (-x[0], x[1]))
    for j in range(N):
        v1 = A[scores[2 * j][1]][i]
        v2 = A[scores[2 * j + 1][1]][i]
        if v1 == v2:
            continue
        if (v1 == 'G' and v2 == 'C') or (v1 == 'C' and v2 == 'P') or (v1 == 'P' and v2 == 'G'):
            scores[2 * j][0] += 1
        else:
            scores[2 * j + 1][0] += 1
scores.sort(key=lambda x: (-x[0], x[1]))
for _, i in scores:
    print(i + 1)
