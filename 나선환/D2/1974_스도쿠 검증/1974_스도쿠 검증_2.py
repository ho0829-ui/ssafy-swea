import sys
sys.stdin = open("input.txt", "r")

# 10개의 스도쿠 게임 만듬
T = int(input())
for test_case in range(1, T + 1):
    puzzle = []
    for i in range(9):
        raw_data = list(map(int, input().split()))
        puzzle.append(raw_data)

    result = 1

# 가로열 검증
    for row in puzzle:
        row_nums = []
        for num in row:
            if num in row_nums:
                result = 0
                break
            else:
                row_nums.append(num)

# 세로열 검증
    if result == 1:
        for c in range(9):
            col_nums = []
            for r in range(9):
                column_num = puzzle[r][c]
                if column_num in col_nums:
                    result = 0
                    break
                else:
                    col_nums.append(column_num)

# 3x3 범위 검증
    if result == 1:
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box_nums = []
                for i in range(3):
                    for j in range(3):
                        num = puzzle[r + i][c + j]
                        if num in box_nums:
                            result = 0
                            break
                        else:
                            box_nums.append(num)

    print(f"#{test_case} {result}")




