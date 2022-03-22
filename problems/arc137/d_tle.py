N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = []
cur = [1] * N
d = {}
for i in range(M):
    tmp = 0
    key = 0
    for j, v in enumerate(cur[::-1]):
        if v:
            tmp ^= A[j]
            key += 2 ** j
    if d.get(key):
        j = d[key]
        cnt = i
        while cnt < M:
            ans.append(ans[j + (cnt - i) % (i - j)])
            cnt += 1
        print(*ans)
        exit()

    d[key] = i
    ans.append(tmp)
    for j in range(N - 1):
        cur[j + 1] = (cur[j] + cur[j + 1]) % 2


print(*ans)
