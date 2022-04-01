n = int(input())
A = list(map(int, input().split()))

max_i, min_i = A.index(max(A)), A.index(min(A))
if min_i == 0 and max_i == n - 1:
    ans = 0
else:
    if max_i > min_i:
        ans = min(min_i + 2, n - max_i + 1)
    else:
        ans = min(max_i + 1, n - min_i + 2)
print(ans)