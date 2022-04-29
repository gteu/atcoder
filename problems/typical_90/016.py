N = int(input())
A, B, C = sorted(list(map(int, input().split())), reverse=True)

ans = 10 ** 5
for i in range(10000):
    for j in range(10000 - i):
        v = A * i + B * j
        if N >= v and (N - v) % C == 0:
            ans = min(ans, i + j + (N - v) // C)
print(ans)
