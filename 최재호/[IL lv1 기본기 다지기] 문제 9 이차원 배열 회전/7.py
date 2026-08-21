import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
matrix = []
matrix=[list(map(int, input().split())) for _ in range(N)]
new_matrix = [[None] * N for _ in range(M)]  # M*N 2차원 빈공간 배열 만들기
for i in range(N):
    N -= 1
    for j in range(M):
        new_matrix[j][N] = matrix[i][j] # 90도 이동한 코드 구현

for i in range(M):
    print(*new_matrix[i]) # 리스트 줄에 있는 값들 출력