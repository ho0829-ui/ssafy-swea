import sys
sys.stdin = open('sample_input.txt', 'r')

def solve(idx, cost):
    global min_cost

    if cost >= min_cost:
        return

    if idx == N:
        min_cost = min(min_cost, cost)
        return

    for i in range(N):
        # 물품 정하면 다음 물품 생산 하러 감
        if not visited[i]:
            visited[i] = 1
            solve(idx + 1, cost + cost_l[idx][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost_l = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_cost = 1485
    solve(0, 0)

    print(f'#{tc} {min_cost}')
