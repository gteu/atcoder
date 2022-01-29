a = int(input())
b = int(input())

if b % 2:
    b = b * 10 // 2
else:
    b = b // 2
print(str(a) + "0" + str(b))