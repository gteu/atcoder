N = int(input())
S = list(input())
Q = int(input())
is_rev = False
for _ in range(Q):
    T, A, B = map(int, input().split())
    A -= 1
    B -= 1
    if T == 1:
        if is_rev:
            S[(A + N) % (2 * N)], S[(B + N) % (2 * N)]\
                = S[(B + N) % (2 * N)], S[(A + N) % (2 * N)]
        else:
            S[A], S[B] = S[B], S[A]
    else:
        is_rev = not is_rev
if is_rev:
    S = S[N:] + S[:N]
print("".join(S))
