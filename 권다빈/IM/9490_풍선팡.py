import sys
sys.stdin = open('9490_풍선팡.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flowers = 0

    for i in range(N):
        for j in range(M):
            cnt_flowers = 0
            for di, dj in ([0,1],[1,0],[0,-1],[-1,0]):
                std_flower = arr[i][j] # 기준점 꽃가루 개수

                for p in range(1, std_flower+1): # 기준점 꽃가루 개수만큼 더 날릴 수 있음
                    ni, nj = i+di*p, j+dj*p

                    if 0<=ni<N and 0<=nj<M:
                        cnt_flowers += arr[ni][nj]
            cnt_flowers += std_flower

            if cnt_flowers > max_flowers:
                max_flowers = cnt_flowers
    print(f'#{tc} {max_flowers}')

                


