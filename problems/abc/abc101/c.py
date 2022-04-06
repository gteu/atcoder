N, K = map(int, input().split())
_ = list(map(int, input().split()))

print((N - K - 1) // (K - 1) + 2)
