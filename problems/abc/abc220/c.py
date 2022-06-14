N = int(input())
A = list(map(int, input().split()))
X = int(input())
s = sum(A)
ans = X // s * N
X %= s
i = 0
while X >= A[i]:
    X -= A[i]
    i += 1
ans += i
print(ans + 1)
