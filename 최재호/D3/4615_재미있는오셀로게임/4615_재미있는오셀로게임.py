import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

# 8방향 델타
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    # 0:빈, 1:흑, 2:백, 초기 세팅
    mid = N // 2
    board[mid - 1][mid - 1] = 2
    board[mid][mid] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1

    for _ in range(M):
        x, y, color = map(int, input().split())

        r, c = y - 1, x - 1 # 인덱스를 사용하기 위해 x,y 각각 -1
        board[r][c] = color
        opponent = 3 - color # 3에서 1(흑)을 빼면 2(백), 2(백)빼면 1(흑)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            candidates = []

            # 연속된 상대 돌의 좌표를 저장
            while 0 <= nr < N and 0 <= nc < N: # 오셀로 판 안에 있는 동안 반복
                if board[nr][nc] != opponent: # 상대 돌이 아니면 멈춤
                    break

                candidates.append((nr, nc)) # 상대 돌이라면 후보군에 저장
                nr += dr # 8방 델타 순회
                nc += dc

            # 끝에 내 돌이 있어야 뒤집을 수 있음
            if 0 <= nr < N and 0 <= nc < N: # 범위를 벗어나지 않고
                if board[nr][nc] == color: # 탐색이 멈춘 곳이 위치가 내 돌인지 확인
                    for rr, cc in candidates: # 저장된 좌표를 하나씩 꺼내 같은 색으로 바꿈
                        board[rr][cc] = color

    black = sum(row.count(1) for row in board)
    white = sum(row.count(2) for row in board)

    print(f"#{tc} {black} {white}")