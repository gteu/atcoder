N, X = map(int, input().split())
X -= 1
A = list(map(lambda x: int(x) - 1, input().split()))
know = [False] * N
while not know[X]:
    know[X] = True
    X = A[X]
print(sum(know))
