import sys
sys.stdin = open('sample_input.txt', 'r')

def sum_battery(now, cnt, battery):
    global min_battery

    # 모든 구역을 방문했다면
    if cnt == N:
        # 현재 위치 → 사무실 비용까지 더하기
        total = battery + golf[now][0]
        # 최솟값 갱신
        min_battery = min(min_battery, total)
        return

    for n in range(1, N):
        # 아직 방문하지 않은 구역이라면
        if not visited[n]:
            visited[n] = 1 # 방문처리
            sum_battery(n, cnt+1, battery+golf[now][n]) # 다음으로 이동
            # 방문 해제
            visited[n] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    golf = [list(map(int, input().split())) for _ in range(N)]
    # 방문 체크
    visited = [0] * N
    visited[0] = 1 # 0은 사무실
    min_battery = N*100

    sum_battery(0, 1, 0)

    print(f'#{tc} {min_battery}')