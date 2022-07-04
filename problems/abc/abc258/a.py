K = int(input())
H = 21 + K // 60
M = 0 + K % 60
print(str(H).zfill(2) + ':' + str(M).zfill(2))
