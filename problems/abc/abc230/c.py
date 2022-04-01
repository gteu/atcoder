N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

k1_min, k1_max = max(1 - A, 1 - B), min(N - A, N - B)
k2_min, k2_max = max(1 - A, B - N), min(N - A, B - 1)

for i in range(P, Q + 1):
    ret = ""
    for j in range(R, S + 1):
        if i - A == j - B and k1_min <= i - A <= k1_max:
            ret += "#"
        elif i - A == B - j and k2_min <= i - A <= k2_max:
            ret += "#"
        else:
            ret += "."
    print(ret)