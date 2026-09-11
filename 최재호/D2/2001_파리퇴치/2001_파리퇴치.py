import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0

    for i in range(N-M+1): # 결국 M*M칸 만큼 파리를 퇴치 할 예정이니 범위는 (0,N-M+1)
        for j in range(N-M+1):
            sum_flies = 0
            for k in range(M): # 파리채 사이즈
                for l in range(M):
                    sum_flies += arr[i+k][j+l]
            if max_flies < sum_flies:
                max_flies = sum_flies

    print(f'#{tc} {max_flies}')