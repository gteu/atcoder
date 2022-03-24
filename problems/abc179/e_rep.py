N, X, M = map(int, input().split())
nums = [X]
cur = X
d = {}
ans = X
for i in range(1, N):
    cur = pow(cur, 2, M)
    nums.append(nums[-1] + cur)
    ans += cur
    if d.get(cur):
        j = d[cur]
        ans += (nums[i] - nums[j]) * ((N - 1 - i) // (i - j))
        ans += nums[j + (N - 1 - i) % (i - j)] - nums[j]
        print(ans)
        exit()
    else:
        d[cur] = i
print(ans)
