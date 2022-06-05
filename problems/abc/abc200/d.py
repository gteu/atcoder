from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(list)
d[0] = []
for i, a in enumerate(A):
    tmp = defaultdict(list)
    for k, v in d.items():
        if k == 0 and len(v) > 0:
            print('Yes')
            ans = v + [i + 1]
            print(len(ans), *ans)
            ans = [i + 1]
            print(len(ans), *ans)
            exit()
        if (a + k) % 200 in d.keys() and len(d[(a + k) % 200]):
            print('Yes')
            ans = d[(a + k) % 200]
            print(len(ans), *ans)
            ans = v + [i + 1]
            print(len(ans), *ans)
            exit()
        tmp[k] = v
        tmp[(a + k) % 200] = d[k] + [i + 1]
    d = tmp
print('No')
