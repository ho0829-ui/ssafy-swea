import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(maze, r, c):
    if maze[r][c] == 3:
        return 1

    vistited[r][c] = 1

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr = r + dr
        nc = c + dc

        if 0<=nr<N and 0<=nc<N and maze[nr][nc] != 1 and not vistited[nr][nc]:
            if dfs(maze, nr, nc) == 1:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    vistited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r = i
                c = j

    print(f'#{tc} {dfs(maze, r, c)}')
