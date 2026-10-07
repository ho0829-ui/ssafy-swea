import sys
sys.stdin = open('sample_input.txt', 'r')
import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    # 최적의 경로, 최소한의 연료로 이동
    # (0, 0) > (N, N)까지 이동
    # 한칸 이동하면 1의 연료, 이동하면서 높이가 높아진만큼 연료 증가
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0 # 시작점
    pq = [(0, 0, 0)] # cost, row, column

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while pq:
        cost, r, c = heapq.heappop(pq)

        if cost > dist[r][c]: # cost가 최소가 저장된 값보다 크면 그냥 넘어가기
            continue

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            fuel = 1 + max(0, H[nr][nc] - H[r][c]) # 높이가 더 높아진만큼 차이와 기본 연료 1개
            new_cost = cost + fuel # 현재 비용이랑 연료 사용량 더 해서 비용 계산
            if new_cost < dist[nr][nc]: # 비용이 저장된 값보다 작다면 비용 갱신
                dist[nr][nc] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc)) # 하고 값을 push

    print(f'#{tc} {dist[N-1][N-1]}')