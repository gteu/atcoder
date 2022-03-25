N, K = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)
A.sort(reverse=True)

ans = 0
for i, (p, c) in enumerate(zip(A, A[1:])):
    if (p - c) * (i + 1) < K:
        ans += (p + c + 1) * (p - c) * (i + 1) // 2
        K -= (p - c) * (i + 1)
    else:
        q = K // (i + 1)
        r = K % (i + 1)
        ans += q * (2 * p - q + 1) * (i + 1) // 2
        ans += (p - q) * r
        break
print(ans)
