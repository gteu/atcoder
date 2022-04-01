from bisect import bisect_left

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()

left = [0]
right = [0]
for i in range(0, N - 1, 2):
    left.append(left[-1] + H[i + 1] - H[i])
    right.append(right[-1] + H[i + 2] - H[i + 1])

ans = 10 ** 18
for w in W:
    i = bisect_left(H, w)
    if i % 2:
        ans = min(ans, w - H[i - 1] + left[i // 2] +
                  right[N // 2] - right[i // 2])
    else:
        ans = min(ans, H[i] - w + left[i // 2] +
                  right[N // 2] - right[i // 2])
print(ans)
