import sys
sys.stdin = open('4615_재미있는_오셀로_게임.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = 2

    for i in range(M):
        r, c, color = map(int, input().split())

        r -= 1
        c -= 1
        # 내가 놓은 돌
        arr[r][c] = color 
        if color == 1:
            other = 2
        else:
            other = 1

        for di, dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
            ni, nj = r+di, c+dj

            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == other:
                    # 상대 돌이 계속 있는지 확인
                    while 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] == 0:
                            break
                        if arr[ni][nj] == color:
                            # 다시 처음 위치에서 한 칸씩 가면서 뒤집기
                            ni, nj = r+di, c+dj

                            while arr[ni][nj] == other:
                                arr[ni][nj] = color
                                ni += di
                                nj += dj
                            break
                        ni += di
                        nj += dj
# 너무 어렵다...........