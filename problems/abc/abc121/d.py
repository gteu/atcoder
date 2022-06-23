def acc_parity(x):
    parity = ''
    for i in range(40):
        if i == 0:
            parity += '1' if x % 4 == 1 or x % 4 == 2 else '0'
        else:
            parity += '1' if x % (2 ** (i + 1)) % 2 == 0 and x % (2 ** (i + 1)) >= 2 ** i else '0'
    parity = parity[::-1]
    return int(parity, 2)


A, B = map(int, input().split())
if A == 0:
    print(acc_parity(B))
else:
    a_par = acc_parity(A - 1)
    b_par = acc_parity(B)
    print(a_par ^ b_par)
