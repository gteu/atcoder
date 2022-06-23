def get_acc_xor(x):
    if x % 2:
        return (x + 1) // 2 % 2
    else:
        return x ^ (x // 2 % 2)


A, B = map(int, input().split())
if A == 0:
    print(get_acc_xor(B))
else:
    print(get_acc_xor(A - 1) ^ get_acc_xor(B))
