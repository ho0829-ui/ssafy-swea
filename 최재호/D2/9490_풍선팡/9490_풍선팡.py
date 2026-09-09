import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_n = 0

    for r in range(n):
        for c in range(m):
            boom = arr[r][c]
            sum_n = arr[r][c]
            for d in range(4):
                for b in range(1, boom+1):
                    nr = r+(dr[d]*b)
                    nc = c+(dc[d]*b)
                    if 0 <= nr < n and 0 <= nc < m:
                        sum_n += arr[nr][nc]
            if max_n < sum_n:
                max_n = sum_n

    print(f'#{tc} {max_n}')
