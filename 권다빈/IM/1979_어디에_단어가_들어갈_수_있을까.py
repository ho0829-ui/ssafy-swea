import sys
sys.stdin = open('1979_어디에_단어가_들어갈_수_있을까.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        # 마지막 칸이 1인 경우
        if cnt == K:
            ans += 1

    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:
            ans += 1
    print(f'#{tc} {ans}')
