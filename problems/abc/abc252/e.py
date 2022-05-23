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
    acc_d = [INF] * len(G)
    d[s] = 0
    acc_d[s] = 0
    q = [(0, s, -1)]
    ret = []
    cnt = 0
    used = [False] * N
    while cnt < N:
        cur_d, cur_i, cur_e = heappop(q)
        if used[cur_i]:
            continue
        used[cur_i] = True
        cnt += 1
        ret.append(cur_e)
        for nxt_i, w, nxt_e in G[cur_i]:
            nxt_d = cur_d + w
            if not used[nxt_i]:
                heappush(q, (nxt_d, nxt_i, nxt_e))

    return ret[1:]


N, M = map(int, input().split())
to = [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    to[A].append((B, C, i + 1))
    to[B].append((A, C, i + 1))
print(*dij(to, 0))
