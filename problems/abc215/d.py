def prime_decompose(x):
    decomposed = set()
    for i in range(2, int(pow(x, 0.5)) + 1):
        while x % i == 0:
            x //= i
            decomposed.add(i)
    if x > 1:
        decomposed.add(x)
    return decomposed

N, M = map(int, input().split())
A = list(map(int, input().split()))

primes = set()
for a in A:
    primes |= prime_decompose(a)

nums = [False] * M
for prime in primes:
    for i in range(prime, M + 1, prime):
        nums[i - 1] = True

ans = []
for i, num in enumerate(nums):
    if not num:
        ans.append(i + 1)
print(len(ans))
print(*ans, sep = '\n')