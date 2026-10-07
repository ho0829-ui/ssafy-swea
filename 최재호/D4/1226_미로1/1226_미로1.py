import sys
sys.stdin = open('input.txt', 'r')

def bfs(si, sj):
    # visited 생성
    visited = [[0] * 16 for _ in range(16)]
    # 큐 생성
    # 시작점 인큐
    q = [(si, sj)]
    # 시작점 인큐 표시
    visited[si][sj] = 1

    #반복
    while q:
        # 디큐
        ti, tj = q.pop(0)

        if maze[ti][tj] == '3':
            return 1

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti + di, tj + dj
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj]!='1' and visited[ni][nj]==0:
                q.append((ni, nj)) # 인큐
                visited[ni][nj] = 1 # 인큐 표시

    return 0

T = 10
for tc in range(1, T+1):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]

    si, sj = 1, 1 # 시작점 위치치

    result = bfs(si, sj)

    print(f'#{tc} {result}')