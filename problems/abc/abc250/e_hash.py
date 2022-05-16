import random


def get_random(X):
    return {x: random.randint(0, 1 << 64) for x in X}


def acc_hash(X):
    used = set()
    cur = 0
    ret = []
    for x in X:
        if x not in used:
            used.add(x)
            cur ^= hash_d[x]
        ret.append(cur)
    return ret


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hash_d = get_random(set(A) | set(B))
hash_A, hash_B = acc_hash(A), acc_hash(B)
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    if hash_A[x - 1] == hash_B[y - 1]:
        print('Yes')
    else:
        print('No')
