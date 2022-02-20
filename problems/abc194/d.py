N = int(input())

ans = 0
for i in range(N - 1):
    ans += N / (N - 1 - i)
print(ans)
