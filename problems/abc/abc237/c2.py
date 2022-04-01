S = input()
S_r = S.rstrip('a')
suf = len(S) - len(S_r)
S_r_l = S_r.lstrip('a')
pre = len(S_r) - len(S_r_l)
if pre <= suf and S_r_l == S_r_l[::-1]:
    print("Yes")
else:
    print("No")