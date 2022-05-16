from collections import Counter


def get_divisor(x):
    divisor = []
    for i in range(1, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x//i:
                divisor.append(x // i)

    return divisor


N, K = map(int, input().split())
S = input()
D = sorted(get_divisor(N))
for d in D:
    tmp = 0
    for i in range(d):
        cnt = Counter(S[i::d])
        tmp += N // d - cnt.most_common()[0][1]
    if tmp <= K:
        print(d)
        exit()
