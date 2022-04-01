x, y = input().split('.')
y = int(y)
if 0 <= y < 3:
    print(x + '-')
elif 3 <= y < 7:
    print(x)
else:
    print(x + '+')