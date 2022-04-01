N = int(input())
S = input().replace('A', 'BB')
ret = []

for i in range(len(S)):
    if ret and ret[-1] == S[i] == 'B':
        ret.pop()
        ret.append('A')
    else:
        ret.append(S[i])
print(''.join(ret))
