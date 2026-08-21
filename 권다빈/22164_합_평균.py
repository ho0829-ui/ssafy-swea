# 다음과 같은 입력이 주어졌을 때, 이 숫자들의 합과 평균을 계산하여 출력하는 프로그램을 작성하세요.
# input
# 5
# 1 2 3 4 5

# output
# 15 3

n = int(input())
numbers = list(map(int, input().split()))
total = 0
avg = 0

for number in numbers:
    total += number

avg = total // len(numbers)

print(total, avg)