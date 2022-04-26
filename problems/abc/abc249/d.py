from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
ans = 0
S = set(A)
for a in S:
    for i in range(1, int(pow(a, 0.5)) + 1):
        if a % i == 0:
            if i in cnt.keys() and a // i in cnt.keys():
                if a // i == i:
                    ans += cnt[a // i] * cnt[i] * cnt[a]
                else:
                    ans += cnt[a // i] * cnt[i] * cnt[a] * 2
print(ans)
