import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 8방향 delta 생성
    delta = [(-1, -1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total_cnt = 0

    for r in range(n):
        for c in range(m):
            current_location = arr[r][c]
            cnt = 0
            for d in range(8):
                dr, dc = r+delta[d][0], c+delta[d][1]
                if 0 <= dr < n and 0 <= dc < m and current_location-arr[dr][dc] > 0:
                    cnt += 1
            if cnt >= 4:
                total_cnt += 1

    print(f'#{tc} {total_cnt}')
