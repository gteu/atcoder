def make_prime(n):
    # n未満の素数を返す
    is_prime = [False] * (n)
    is_prime[2] = True
    for i in range(3, n, 2):
        is_prime[i] = True
    m = int(n ** 0.5) + 1
    for p in range(3, m, 2):
        if is_prime[p]:
            for q in range(p * p, n, p + p):
                is_prime[q] = False

    ret = []
    for i in range(n):
        if is_prime[i]:
            ret.append(i)

    return ret


p = make_prime(201)
A, B, C, D = map(int, input().split())
for i in range(A, B + 1):
    flag = True
    for j in range(C, D + 1):
        if i + j in p:
            flag = False
    if flag:
        print('Takahashi')
        exit()
print('Aoki')
