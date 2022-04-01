from functools import lru_cache

MOD = 998244353
X = int(input())


@lru_cache(maxsize=None)
def dfs(n):
    if n > 4:
        if n % 2:
            return dfs(n // 2) * dfs(n // 2 + 1) % MOD
        else:
            return dfs(n // 2) * dfs(n // 2) % MOD
    else:
        return n


print(dfs(X))
