T = int(input())

for test_case in range(1, T + 1):
    numbers = [list(map(int, input().split())) for _ in range(9)]
    has_duplicate = False

    # 3*3 같은 숫자있는지 확인
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = []
            for r in range(i, i+3):
                block.extend(numbers[r][j:j+3])
            if len(set(block)) != 9:
                has_duplicate = True

    # 한줄에 같은 숫자 있는지 확인

    # 가로줄 검사
    for i in range(9):
            if len(set(numbers[i])) != 9:
                has_duplicate = True

    # 세로 줄 검사
    for i in range(9):
        column = []
        for j in range(9):
            column.append(numbers[j][i])
        if len(set(column)) != 9:
            has_duplicate = True

    if has_duplicate:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')
