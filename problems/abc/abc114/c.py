from itertools import product
N = int(input())
ans = 0
for i in range(1, 10):
    for v in product('357', repeat=i):
        used = [False] * 3
        for j in range(i):
            used['357'.index(v[j])] = True
        if all(used) and int(''.join(v)) <= N:
            ans += 1
print(ans)
