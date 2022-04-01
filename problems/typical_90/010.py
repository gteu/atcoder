import sys
input = sys.stdin.readline

N = int(input())
acc = [[-1] for _ in range(2)]
for _ in range(N):
    C, P = map(int, input().split())
    if C == 1:
        acc[0].append(acc[0][-1] + P)
        acc[1].append(acc[1][-1])
    else:
        acc[1].append(acc[1][-1] + P)
        acc[0].append(acc[0][-1])

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    print(acc[0][R] - acc[0][L], acc[1][R] - acc[1][L])
