i, j = map(int, input().split())
s = input()
print(s[:i-1] + s[i-1:j][::-1] + s[j:])