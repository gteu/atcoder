def dij(G, s):
    """Dijkstra's algorithm
    Args:
        G (List[List[int, int]]): [adjacent node, weight] 
        s (int): starting index

    Returns:
        d (List[int]): distances
    """
    from heapq import heappush, heappop

    INF = 10 ** 18
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


N, M = map(int, input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    to[A].append((B, C))
    to[B].append((A, C))

ds = dij(to, 0)
de = dij(to, N - 1)

for i in range(N):
    print(ds[i] + de[i])
