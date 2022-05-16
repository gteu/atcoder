N, A, B = map(int, input().split())
ans = []
for i in range(A * N):
    tmp = ''
    for j in range(B * N):
        if (i // A + j // B) % 2 == 0:
            tmp += '.'
        else:
            tmp += '#'
    ans.append(tmp)
print(*ans, sep='\n')
