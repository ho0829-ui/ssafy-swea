# 첫 줄에 두 개의 정수 N과 K가 주어집니다. N은 배열의 크기, K는 부분 배열의 크기입니다.
# 두 번째 줄에 N개의 정수가 공백으로 구분되어 주어집니다.
# 이 배열에서 연속된 K개의 원소로 이루어진 부분 배열 중 그 합이 최대인 것을 찾아 그 합을 출력하는 프로그램을 작성하세요.

# input
# 8 3
# 1 2 3 4 5 6 7 8

# output
# 21

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
max_sum = 0
total = 0

for i in range(n-2):
    total = numbers[i] + numbers[i+1] + numbers[i+2]
    if max_sum < total:
        max_sum = total

print(max_sum)
