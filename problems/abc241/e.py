N, K = map(int, input().split())
A = list(map(int, input().split()))
count = [[0, -1] for _ in range(N)]
can = 0
cur = 0
flag = False

while cur < K:
    cur += 1
    can += A[can % N]
    if count[can % N][1] != -1 and not flag:
        can += ((K - count[can % N][1]) // (cur - count[can %
                N][1]) - 1) * (can - count[can % N][0])
        cur += ((K - count[can % N][1]) // (cur -
                count[can % N][1]) - 1) * (cur - count[can % N][1])
        flag = True
    count[can % N] = [can, cur]

print(can)
