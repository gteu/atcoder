N, Q = map(int, input().split())
S = input()
cur = 0
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        cur = (cur - x) % N
    else:
        print(S[(cur + x - 1) % N])
