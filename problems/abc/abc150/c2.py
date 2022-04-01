import itertools


def get_index(S):
    for i, T in enumerate(itertools.permutations(range(1, N + 1))):
        if S == T:
            return i


N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

print(abs(get_index(P) - get_index(Q)))
