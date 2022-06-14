X = input()
d = {}
for i in range(26):
    c = chr(ord('a') + i)
    d[X[i]] = c

N = int(input())
strs = []
for _ in range(N):
    S = input()
    tmp = ''
    for s in S:
        tmp += d[s]
    strs.append((tmp, S))
strs.sort()
for _, s in strs:
    print(s)
