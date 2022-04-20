import sys


def dij(G, s):
    """Dijkstra's algorithm
    Args:
        G (List[List[int, int]]): [adjacent node, weight] 
        s (int): starting index

    Returns:
        d (List[int]): distances
    """
    from heapq import heappush, heappop

    d = [INF] * len(G)
    d[s] = 0
    q = [(0, s)]
    while q:
        cur_d, cur_i = heappop(q)
        if cur_d > d[cur_i]:
            continue
        for nxt_i, w in G[cur_i]:
            nxt_d = cur_d + w
            if d[nxt_i] > nxt_d:
                d[nxt_i] = nxt_d
                heappush(q, (nxt_d, nxt_i))
    return d


input = sys.stdin.readline
INF = 10 ** 18
N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    edges[A].append((B, C))


ds = []
for i in range(N):
    ds.append(dij(edges, i))

for i in range(N):
    ans = INF
    for nxt_i, w in edges[i]:
        if nxt_i == i:
            ans = min(ans, w)

    for j in range(N):
        if ds[i][j] == INF or ds[j][i] == INF:
            continue
        elif i != j:
            ans = min(ans, ds[i][j] + ds[j][i])
    if ans == INF:
        print(-1)
    else:
        print(ans)
