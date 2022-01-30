def dij(G, s):
    from heapq import heappush, heappop

    INF = 10 ** 18
    D = [INF] * len(G)
    D[s] = 0
    q = [(0, s)]
    while q:
        cur_d, cur_i = heappop(q)
        if cur_d > D[cur_i]:
            continue
        for nxt_i, w in G[cur_i]:
            nxt_d = cur_d + w
            if D[nxt_i] > nxt_d:
                D[nxt_i] = nxt_d
                heappush(q, (nxt_d, nxt_i))
    return D
    
N, M = map(int, input().split())
H = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    U, V = map(lambda x: int(x) - 1, input().split())
    if H[U] < H[V]:
        G[U].append((V, (H[V] - H[U])))
        G[V].append((U, 0))
    elif H[U] > H[V]:
        G[V].append((U, (H[U] - H[V])))
        G[U].append((V, 0))
    else:
        G[U].append((V, 0))
        G[V].append((U, 0))
dist = dij(G, 0)
print(max(H[0] - H[i] - dist[i] for i in range(N)))
