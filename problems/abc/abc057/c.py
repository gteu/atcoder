def get_divisor(x):
    divisor = []
    for i in range(1, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x//i:
                divisor.append(x // i)

    return divisor


N = int(input())
ans = 10 ** 10
for i in range(1, int(pow(N, 0.5)) + 1):
    if N % i == 0:
        ans = min(ans, len(str(N//i)))
print(ans)
