n = int(input())
A = list(map(int, input().split()))

if n % 2:
    print("Win")
else:
    v = 0
    for a in A:
        v ^= a

    if any([a == v for a in A]):
        print("Win")
    else:
        print("Lose")