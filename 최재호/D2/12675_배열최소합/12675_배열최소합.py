import sys
sys.stdin = open('sample_input.txt', 'r')

def solve(idx):
    global min_v
    if idx == N:
        sum_v = sum(selected)
        if sum_v < min_v:
            min_v = sum_v
        return
    for i in range(N):
        if check[i] == 0:
            selected[idx] = rows[idx][i]
            check[i] = 1
            solve(idx+1)
            check[i] = 0

def solve2(idx, sum_v):
    global min_v
    if sum_v > min_v:
        return
    if idx == N:
        if sum_v < min_v:
            min_v = sum_v
        return
    for i in range(N):
        if check[i] == 0:
            selected[idx] = rows[idx][i]
            check[i] = 1
            solve2(idx+1, sum_v + rows[idx][i])
            check[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rows = [list(map(int, input().split())) for _ in range(N)]

    selected = [0] * N
    check = [0] * N
    min_v = 10 * N
    solve2(0 ,0)
    print(f'#{tc} {min_v}')