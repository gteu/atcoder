from collections import deque, defaultdict

M = int(input())
to = [[] for _ in range(10)]

for _ in range(M):
    u, v = map(int, input().split())
    to[u].append(v)
    to[v].append(u)

p = input().replace(' ', '')
if p == '12345678':
    print(0)
    exit()
q = deque([p])
d = defaultdict(int)
d[p] = 0
while q:
    cur = q.pop()
    for i in range(1, 10):
        if str(i) not in cur:
            for j in to[i]:
                ji = cur.index(str(j))
                nxt = list(cur)
                nxt[ji] = str(i)
                nxt = ''.join(nxt)
                if nxt == '12345678':
                    print(d[cur] + 1)
                    exit()
                if not d[nxt]:
                    q.appendleft(nxt)
                    d[nxt] = d[cur] + 1

print(-1)
