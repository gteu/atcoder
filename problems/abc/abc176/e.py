from collections import defaultdict
import sys
input = sys.stdin.readline


H, W, M = map(int, input().split())
hd = defaultdict(int)
wd = defaultdict(int)
bombers = set()
for _ in range(M):
    h, w = map(int, input().split())
    hd[h] += 1
    wd[w] += 1
    bombers.add((h, w))

hc = sorted(hd.items(), key=lambda x: x[1], reverse=True)
wc = sorted(wd.items(), key=lambda x: x[1], reverse=True)

hi = set()
wi = set()
for h, c in hc:
    if c == hc[0][1]:
        hi.add(h)
    else:
        break
for w, c in wc:
    if c == wc[0][1]:
        wi.add(w)
    else:
        break

cnt = 0
for h, w in bombers:
    if h in hi and w in wi:
        cnt += 1
if cnt == len(hi) * len(wi):
    print(hc[0][1] + wc[0][1] - 1)
else:
    print(hc[0][1] + wc[0][1])
