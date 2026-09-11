import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split()) # 첫줄 인자 2개 받아오기

matrix = [list(map(int, input().split())) for _ in range(N)] # N * M 행렬 만들기

sum_num = 0

for i in range(N): # 반복문으로 행렬 합 구하기
    for j in range(M):
        sum_num += matrix[i][j]

print(sum_num)