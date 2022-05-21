N = int(input())
S = list(map(int, input().split()))
cand = set()
for i in range(1, 200):
    for j in range(1, 200):
        cand.add(4 * i * j + 3 * i + 3 * j)

ans = 0
for s in S:
    if s not in cand:
        ans += 1
print(ans)
