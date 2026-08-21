# 첫 줄에는 행의 수 N과 열의 수 M이 주어집니다.
# 그 다음 N개의 줄에 각각 M개의 정수가 공백으로 구분되어 주어집니다.
# 이 2차원 배열의 모든 원소의 합을 계산하여 출력하는 프로그램을 작성하세요.

# input
# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# output
# 78

n, m = map(int, input().split())
total = 0

for i in range(n):
    numbers = list(map(int, input().split()))
    for j in range(m):
        total += numbers[j]
print(total)