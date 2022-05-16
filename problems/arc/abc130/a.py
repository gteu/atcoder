N = int(input())
S = input()

ans = 0
cnt = 1
pre = S[0]
for s in S[1:]:
    if pre == s:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2
        cnt = 1
    pre = s
ans += cnt * (cnt - 1) // 2
print(ans)
