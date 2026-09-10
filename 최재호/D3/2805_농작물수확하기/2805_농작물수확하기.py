import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]

    mid = N // 2 # N은 항상 홀수
    start = end = mid # 처음 시작 범위는 가운데 1칸이니 시작점 중간점 끝점이 같음
    harvest = 0

    for i in range(N):
        for j in range(start, end + 1):
            harvest += farm[i][j]

        if i < mid: # 행이 가운데에 도달하기 전까지 범위를 늘려감
            start -= 1
            end += 1
        else: # 행의 중앙 부분부터 크기가 1까지 점점 작아짐
            start += 1
            end -= 1

    print(f'#{tc} {harvest}')