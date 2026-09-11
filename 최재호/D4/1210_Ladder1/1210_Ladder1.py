import sys
sys.stdin = open("input.txt", "r")

T = 10

def solve(ladder):
    # 상 좌 우
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    # 시작은 값이 2인 열에서 시작
    r = 99
    c = 0
    for i in range(100): # 시작점 열 찾기 반복문
        if ladder[r][i] == 2:
            c = i
            break
    d = 0 # 현재 이동하는 방향을 저장하는 변수
    while r > 0:
        if d == 0:
            if c-1 >= 0 and ladder[r][c-1] == 1: # 왼쪽에 길이 있음
                d = 1
            if c+1 <= 99 and ladder[r][c+1] == 1: # 오른쪽에 길이 있음
                d = 2
        elif d == 1: # 왼쪽
            # 윗 방향 살펴보고 갈 수 있으면 방향바꾸기
            if ladder[r-1][c] == 1:
                d = 0
        else: # 오른쪽
            if ladder[r-1][c] == 1:
                d = 0
        # 방향대로 한 칸 이동하기
        r += dr[d]
        c += dc[d]

    return c

for tc in range(1, T+1):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    result = solve(ladder)

    print(f'#{tc} {result}')

