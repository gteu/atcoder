from collections import Counter

N = int(input())
V = list(map(int, input().split()))

cnt1 = sorted(Counter(V[::2]).items(), key=lambda x: x[-1], reverse=True)
cnt2 = sorted(Counter(V[1::2]).items(), key=lambda x: x[-1], reverse=True)

if cnt1[0][0] == cnt2[0][0]:
    if len(cnt2) > 1:
        ans = N - cnt1[0][1] - cnt2[1][1]
    else:
        ans = N - cnt1[0][1]
    if len(cnt1) > 1:
        ans = min(ans, N - cnt2[0][1] - cnt1[1][1])
    else:
        ans = min(ans, N - cnt2[0][1])
else:
    ans = N - cnt1[0][1] - cnt2[0][1]
print(ans)
