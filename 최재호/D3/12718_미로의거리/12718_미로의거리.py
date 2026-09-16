import sys
sys.stdin = open('sample_input.txt', 'r')

def find_starting_point(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j

def bfs(si, sj):
    # 초기화
    # visited 생성
    visited = [[0]*N for _ in range(N)]
    # 큐 and 시작점 인큐
    q = [(si, sj)]
    # 시작점 인큐 표시
    visited[si][sj] = 1

    # 미로 찾을 때 까지 반복
    while q:
        # 디큐
        ti, tj = q.pop(0)

        if maze[ti][tj] == '3':
            return visited[ti][tj] - 2

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti + di, tj + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!='1' and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ti][tj] + 1

    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    si, sj = find_starting_point(maze)

    result = bfs(si, sj)

    print(f'#{tc} {result}')