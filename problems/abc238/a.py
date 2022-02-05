def yes(bool):
    if bool:
        print("Yes")
    else:
        print("No")

N = int(input())
yes(pow(2, N) > pow(N, 2))