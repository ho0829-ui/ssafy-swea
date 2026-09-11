import sys
sys.stdin = open('2001_파리퇴치.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for p in range(M):
                for q in range(M):
                    cnt += arr[i+p][j+q]

            if cnt > ans:
                ans = cnt
    print(f'#{tc} {ans}')