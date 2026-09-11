import sys
sys.stdin = open("input.txt", "r")


for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cells = 100
    sum_n = []

    # 행의 합 더하기
    for i in range(cells):
        sum_row = 0
        for j in range(cells):
            sum_row += arr[i][j]
        sum_n.append(sum_row)

    # 열의 합 더하기
    for j in range(cells):
        sum_col = 0
        for i in range(cells):
            sum_col += arr[i][j]
        sum_n.append(sum_col)

    # 대각선의 합 더하기
    sum_left_dia = 0
    for i in range(cells):
        sum_left_dia += arr[i][i]
    sum_n.append(sum_left_dia)

    sum_right_dia = 0
    for i in range(cells):
        sum_right_dia += arr[i][cells-1-i]
    sum_n.append(sum_right_dia)

    max_n = sum_n[0]
    for k in range(len(sum_n)):
        if max_n < sum_n[k]:
            max_n = sum_n[k]

    print(f'#{t} {max_n}')

