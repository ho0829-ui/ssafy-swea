import sys
sys.stdin = open('16268_풍선팡2.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flowers = 0

    for i in range(N):
        for j in range(M):
            cnt_flowers = 0
            for di, dj in ([0,1],[1,0],[0,-1],[-1,0]):
                ni, nj = i+di, j+dj

                if 0<=ni<N and 0<=nj<M:
                    cnt_flowers += arr[ni][nj]
            cnt_flowers += arr[i][j]

            if cnt_flowers > max_flowers:
                max_flowers = cnt_flowers
    print(f'#{tc} {max_flowers}')

