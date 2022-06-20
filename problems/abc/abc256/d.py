N = int(input())
L = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append((l, r))
L.sort()
ans = []
cur_l, cur_r = L[0]
for l, r in L[1:]:
    if cur_r < l:
        ans.append((cur_l, cur_r))
        cur_l, cur_r = l, r
    else:
        cur_l = min(cur_l, l)
        cur_r = max(cur_r, r)
ans.append((cur_l, cur_r))
ans.sort()
for l, r in ans:
    print(l, r)
