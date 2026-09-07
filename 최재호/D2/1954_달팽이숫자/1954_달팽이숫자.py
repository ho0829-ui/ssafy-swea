import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    i,j = 0, 0
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    num = 1
    d = 0
    while num <= n**2:
        arr[i][j] = num
        i += move[d][0]
        j += move[d][1]

        if i < 0 or i >= n or j < 0 or j >= n or arr[i][j] != 0:
            i -= move[d][0]
            j -= move[d][1]
            d = (d+1)%4
            i += move[d][0]
            j += move[d][1]
        num += 1
    print(f'#{tc}')
    for row in arr:
        print(*row)