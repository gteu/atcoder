N = int(input())
not_used = set(range(1, 2 * N + 2))
while -1:
    print(not_used.pop())
    v = int(input())
    if v == 0:
        break
    not_used.remove(v)

exit()
