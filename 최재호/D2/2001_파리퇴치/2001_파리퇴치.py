import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_flies = 0
            for k in range(M):
                for l in range(M):
                    sum_flies += arr[i+k][j+l]
            if max_flies < sum_flies:
                max_flies = sum_flies

    print(f'#{tc} {max_flies}')