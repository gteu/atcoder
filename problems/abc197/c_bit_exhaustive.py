N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 18

for i in range(2 ** N):
    cur_or, cur_xor = 0, 0
    for j in range(N):
        if i >> j & 1:
            cur_xor ^= cur_or
            cur_or = A[j]
        else:
            cur_or |= A[j]
    ans = min(ans, cur_or ^ cur_xor)
print(ans)
