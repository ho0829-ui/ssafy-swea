import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input()) # 1 ≤ T ≤ 50

for test_case in range(1, T + 1):
    N = int(input()) #  5 ≤ N ≤ 1000
    arr = list(map(int, input().split()))
    ans = 0
    min_num = arr[0]
    max_num = arr[0]
    for i in range(N):
        if max_num <= arr[i]:
            max_num = arr[i]
        if min_num >= arr[i]:
            min_num = arr[i]
    ans = max_num - min_num

    print(f'#{test_case} {ans}')