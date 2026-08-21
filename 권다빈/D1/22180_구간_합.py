# 첫 줄에 두 개의 정수 N과 M이 주어집니다. N은 배열의 크기, M은 구간의 개수입니다.
# 두 번째 줄에 N개의 정수가 공백으로 구분되어 주어집니다.
# 그 다음 M개의 줄에 각각 두 개의 정수 i와 j가 주어집니다.

# 배열의 i번째 수부터 j번째 수까지의 합을 각 줄마다 출력하는 프로그램을 작성하세요. (인덱스는 1부터 시작합니다)

# input
# 5 3
# 1 2 3 4 5
# 1 3
# 2 4
# 3 5

# output
# 6
# 9
# 12

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
total = 0

for _ in range(m):
    i, j = map(int, input().split())
    total = sum(numbers[i-1:j])
    print(total)