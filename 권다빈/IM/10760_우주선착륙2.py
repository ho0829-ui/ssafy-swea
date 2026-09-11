import sys
sys.stdin = open('10760_우주선착륙2.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0 # 예비 후보지

    for i in range(N):
        for j in range(M):
            std_num = arr[i][j] # 1
            cand_area = 0 
            for di, dj in ([0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]):
                ni, nj = i+di, j+dj

                if 0<=ni<N and 0<=nj<M:
                    if arr[ni][nj] < std_num:
                        cand_area += 1

            
            if cand_area >= 4:
                ans += 1
    print(f'#{tc} {ans}')
