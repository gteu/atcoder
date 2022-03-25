N = int(input())
A = list(map(int, input().split()))
print(sum(map(lambda x: x - 1, A)))
