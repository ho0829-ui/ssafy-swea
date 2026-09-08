import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i-1]
        new_row = [1]
        for j in range(1, i):
            value = prev_row[j-1] + prev_row[j]
            new_row.append(value)
        new_row.append(1)
        triangle.append(new_row)

    print(f'#{tc}')
    for row in triangle:
        print(' '.join(map(str, row)))
