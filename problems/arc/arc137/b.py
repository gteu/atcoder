N = int(input())
A = list(map(int, input().split()))

acc = [0]
for a in A:
    if a == 0:
        acc.append(acc[-1] + -1)
    else:
        acc.append(acc[-1] + 1)

maxs = [0] * (N + 1)
mins = [0] * (N + 1)
cur_max = acc[-1]
cur_min = acc[-1]
for i in range(N, -1, -1):
    cur_max = max(cur_max, acc[i])
    cur_min = min(cur_min, acc[i])
    maxs[i] = cur_max
    mins[i] = cur_min

ans_max = -10 ** 9
ans_min = 10 ** 9
for i in range(N):
    ans_max = max(ans_max, maxs[i] - acc[i])
    ans_min = min(ans_min, mins[i] - acc[i])
print(ans_max - ans_min + 1)
