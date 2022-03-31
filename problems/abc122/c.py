N, Q = map(int, input().split())
S = input()
acc = [0]
for p, c in zip(S, S[1:]):
    if p == 'A' and c == 'C':
        acc.append(acc[-1] + 1)
    else:
        acc.append(acc[-1])

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(acc[r] - acc[l])
