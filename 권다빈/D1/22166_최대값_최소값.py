# input
# 7
# 8 3 12 7 5 11 2

# output
# 12 2

n = int(input())
numbers = list(map(int, input().split()))
min_num = 1000000
max_num = 0

for number in numbers:
    if min_num > number:
        min_num = number
    if max_num < number:
        max_num = number
print(max_num, min_num) 