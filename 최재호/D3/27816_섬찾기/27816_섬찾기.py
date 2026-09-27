import sys
sys.stdin = open('sample_in.txt', 'r')

from collections import deque


def bfs(si, sj, arr, visited, N, M):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ti, tj = q.popleft()

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = ti + di
            nj = tj + dj

            if (
                0 <= ni < N
                and 0 <= nj < M
                and arr[ni][nj] == 'L'
                and visited[ni][nj] == 0
            ):
                visited[ni][nj] = 1
                q.append((ni, nj))


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    cnt_land = 0

    for i in range(N):
        for j in range(M):

            # 새로운 섬 발견
            if arr[i][j] == 'L' and visited[i][j] == 0:
                cnt_land += 1

                # 해당 섬 전체 방문 처리
                bfs(i, j, arr, visited, N, M)

    print(f'#{tc} {cnt_land}')