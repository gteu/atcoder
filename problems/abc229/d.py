S = input()
K = int(input())

dot = [-1]
for i in range(len(S)):
    if S[i] == ".":
        dot.append(i)
dot.append(len(S))

ret = 0
for i in range(len(dot)):
    if i + K + 1 < len(dot):
        ret = max(ret, dot[i+K+1] - dot[i] - 1)
    else:
        ret = max(ret, dot[-1] - dot[i] - 1)

print(ret)