import sys
sys.stdin = open('input.txt', 'r')

def check_sudoku(board):
    # 행 검사
    for row in board:
        if len(set(row)) != 9:
            return 0

    # 열 검사
    for col in zip(*board):
        if len(set(col)) != 9:
            return 0

    # 3x3 검사
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            box = []
            for k in range(r, r+3):
                for l in range(c, c+3):
                    box.append(board[k][l])
            if len(set(box)) != 9:
                return 0
    return 1

T = int(input())

for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]

    result = check_sudoku(board)

    print(f'#{tc} {result}')