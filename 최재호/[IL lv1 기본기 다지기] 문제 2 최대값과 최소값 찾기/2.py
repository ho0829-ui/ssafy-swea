import sys
sys.stdin = open("input.txt", "r")

n = int(input()) # 1번째줄 input
arr = []
arr = list(map(int, input().split())) # 2번째줄 input

max_num = arr[0]
min_num = arr[0]

for i in range(n): # max값
    if max_num < arr[i]:
        max_num = arr[i]
for i in range(n): # min값
    if min_num > arr[i]:
        min_num = arr[i]

print(max_num, min_num)