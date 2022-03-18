import math


def get_index(S):
    cnt = 1
    used = [False] * N
    for i in range(N - 1):
        for j in range(N):
            if S[i] == j + 1:
                break
            if not used[j]:
                cnt += math.factorial(N - i - 1)
        used[S[i] - 1] = True
    return cnt


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
print(abs(get_index(P) - get_index(Q)))
