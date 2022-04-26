A, B, C, D, E, F, X = map(int, input().split())
ad, bd = 0, 0
ax, bx = X, X
while ax > 0:
    ad += min(A, ax) * B
    ax -= min(A, ax)
    ax -= C

while bx > 0:
    bd += min(D, bx) * E
    bx -= min(D, bx)
    bx -= F

if ad > bd:
    print('Takahashi')
elif ad < bd:
    print('Aoki')
else:
    print('Draw')
