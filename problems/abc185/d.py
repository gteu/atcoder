N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = [0] + A + [N + 1]

blue = []
for p, c in zip(A, A[1:]):
    if c - p > 1:
        blue.append(c - p - 1)

ans = 0
if not blue:
    print(ans)
else:
    min_blue = min(blue)
    for b in blue:
        ans += (b - 1) // min_blue + 1
    print(ans)
