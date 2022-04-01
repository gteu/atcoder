def get_divisor(x):
    divisor = []
    for i in range(1, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x//i:
                divisor.append(x // i)

    return divisor


N = int(input())
D = get_divisor(N)
ans = 0
for d in D:
    if d % 2:
        ans += 2
print(ans)
