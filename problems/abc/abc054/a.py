a, b = map(int, input().split())
if a == 1:
    a += 13
if b == 1:
    b += 13
if a > b:
    print('Alice')
elif a < b:
    print('Bob')
else:
    print('Draw')
