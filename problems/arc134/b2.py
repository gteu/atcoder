n = int(input())
s = list(input())

L, R = 0, n - 1

for i in range(26):
    l, r = L, R
    while l < r:
        if ord(s[l]) <= ord('a') + i:
            l += 1
        elif ord(s[r]) == ord('a') + i:
            s[l], s[r] = s[r], s[l]
            L = l + 1
            R = r - 1
            continue
        else:
            r -= 1

print("".join(s))
