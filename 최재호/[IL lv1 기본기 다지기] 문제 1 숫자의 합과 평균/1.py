import sys
sys.stdin = open("input.txt", "r")

arr = []

n = int(input()) # 첫번째 줄

arr = list(map(int, input().split())) # 두번째 줄

num_sum = 0
num_avg = 0

for i in range(n):
    num_sum += arr[i]

num_avg = num_sum // n

print(num_sum, num_avg)

