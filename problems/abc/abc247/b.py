from collections import defaultdict

N = int(input())
S = defaultdict(int)
names = []
for _ in range(N):
    s, t = input().split()
    names.append((s, t))
    if s != t:
        S[s] += 1
        S[t] += 1
    else:
        S[s] += 1

for s, t in names:
    if S[s] == 1 or S[t] == 1:
        continue
    else:
        print('No')
        exit()
print('Yes')
