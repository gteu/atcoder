N = int(input())
A = list(map(int, input().split()))

cur = [-1] * (2 * 10 ** 5 + 1)
cur_n = [-1] * (2 * 10 ** 5 + 1)
i = 0
j = 0
for a in A:
    if not cur:
        cur[i] = a
        cur_n[j] = 1
        i += 1
    else:
        if a == cur[i - 1]:
            if cur_n[j] == a - 1:
                i -= (a - 1)
                j -= 1
            else:
                cur_n[j] += 1
                cur[i] = a
                i += 1
        else:
            j += 1
            cur_n[j] = 1
            cur[i] = a
            i += 1
    print(i)
