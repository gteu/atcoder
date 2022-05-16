from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))
ans = set()
for i in range(1, 4):
    for p in combinations(A, i):
        if sum(p) <= W:
            ans.add(sum(p))
print(len(ans))
