S = input()
K = int(input())

cnt = [0]
for i in range(len(S)):
    cnt.append(cnt[i] + 1 if S[i] == "." else cnt[i])
r = 0
ans = 0
for l in range(len(cnt) - 1):
    while r < len(cnt) - 1 and cnt[r+1] - cnt[l] <= K:
        r += 1
    ans = max(ans, r - l)
print(ans)