import heapq 

n = int(input())
s = input()
q = []
for i, c in enumerate(s):
    q.append((ord(c), -i))
heapq.heapify(q)

l, r = 0, n - 1 
swap_i = []
while(l < r):
    min_sn, min_i = heapq.heappop(q)
    min_i *= -1
    if ord(s[l]) == min_sn:
        heapq.heappush(q, ((min_sn), -min_i))
        l += 1
        continue
    if min_i < l or min_i > r:
        continue
    if l > min_i:
        break
    swap_i.append((l, min_i))
    r = min_i - 1
    l += 1

s = list(s)
for l, r in swap_i:
    s[l], s[r] = s[r], s[l]
print("".join(s))