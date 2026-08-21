# 첫 줄은 숫자의 개수 N을 나타내고, 두 번째 줄은 N개의 정수가 공백으로 구분되어 주어집니다.
# 각 숫자의 등장 빈도수를 계산하여 출력하는 프로그램을 작성하세요.
# 출력은 숫자와 빈도수를 공백으로 구분하여 한 줄에 하나씩 출력하되, 숫자가 작은 순서대로 출력하세요.

# input
# 8
# 1 2 3 2 1 3 2 1

# output
# 1 3
# 2 3
# 3 2

n = int(input())
numbers = list(map(int, input().split()))
count_number = {}

for number in numbers:
    count_number[number] = count_number.get(number, 0) + 1

for key, value in count_number.items():
    print(key, value)