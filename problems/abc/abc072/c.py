N = int(input())
cnt = [0] * (10 ** 5 + 1)
A = list(map(int, input().split()))
for a in A:
    cnt[a] += 1

ans = 0
for i in range(10 ** 5 - 1):
    ans = max(ans, cnt[i] + cnt[i + 1] + cnt[i + 2])
print(ans)
