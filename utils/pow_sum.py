# 123 = 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 を求めるやつ

n = 123
d = 10 # max 2^10くらいとする
for i in reversed(range(d)):
    l = 1 << i
    if l <= n:
        print(l)
        n -= l