import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(M)]

result_list = []

for k in range(M):
    i, j = matrix[k][0], matrix[k][1]  # matrix를 순회하면서 범위를 i, j에 할당
    sum_num = 0
    for l in range(i-1, j):  # 범위 안에서 더하기 인덱스 신경쓰기
        sum_num += arr[l]
    result_list.append(sum_num)  # 빈 리스트에 범위 더한 값 담기
for o in range(M):
    print(result_list[o])