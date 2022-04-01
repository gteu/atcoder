N = int(input())
A = list(map(int, input().split()))
s = 0
ang = set([0])
for a in A:
    s += a
    ang.add(s % 360)
ans = 0
ang.add(360)
ang = sorted(list(ang))
for p, c in zip(ang, ang[1:]):
    ans = max(ans, c - p)
print(ans)