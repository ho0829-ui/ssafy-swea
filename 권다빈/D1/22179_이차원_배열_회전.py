# 이 2차원 배열을 시계 방향으로 90도 회전한 결과를 출력하는 프로그램을 작성하세요.
# 첫 줄에 두 개의 정수 N과 M이 주어집니다. N은 행의 수, M은 열의 수입니다.
# 그 다음 N개의 줄에 각각 M개의 정수가 공백으로 구분되어 주어집니다.

# input
# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# output
# 9 5 1
# 10 6 2
# 11 7 3
# 12 8 4

n, m = map(int, input().split())
di = [list(map(int, input().split())) for _ in range(n)]

for i in range(m):
    for j in range(n-1, -1, -1):
        print(di[j][i], end=' ')
    print()