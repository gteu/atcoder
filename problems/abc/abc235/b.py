n = int(input())
hs = list(map(int, input().split()))

flag = False
for hp, hc in zip(hs, hs[1:]):
  if hp < hc:
    continue
  else:
    print(hp)
    flag = True
    break
if not flag:
  print(hs[-1])