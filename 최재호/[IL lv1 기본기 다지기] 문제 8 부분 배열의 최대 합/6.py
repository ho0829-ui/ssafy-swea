import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
arr = []
arr = list(map(int, input().split()))

for i in range(N): # for문으로 리스트를 순차적으로 순회하면서 큰 값이면 서로의 리스트 위치를 바꾸는 방식으로 큰 값을 정렬
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

sum_num = 0

for i in range(K): # 상위 K개의 인덱스까지만 합
    sum_num += arr[i]

print(sum_num)