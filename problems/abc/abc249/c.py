N, K = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

ans = 0
for i in range(2 ** N):
    cnt = [0] * 26
    for j in range(N):
        if i >> j & 1:
            for s in S[j]:
                cnt[ord(s) - ord('a')] += 1
    num = 0
    for v in cnt:
        if v == K:
            num += 1
    ans = max(ans, num)
print(ans)
