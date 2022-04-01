from itertools import groupby
N, K = map(int, input().split())
S = input()

rle = []
for k, v in groupby(S):
    rle.append((k, len(list(v))))

j = 0
zero = 0
d = 0
ans = 0
for i in range(len(rle)):
    while zero <= K and j < len(rle):
        if rle[j][0] == '0':
            if zero == K:
                break
            zero += 1
        d += rle[j][1]
        j += 1
        ans = max(ans, d)

    d -= rle[i][1]
    if rle[i][0] == '0':
        zero -= 1

print(ans)
