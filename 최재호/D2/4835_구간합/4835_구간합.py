import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input()) # 1 ≤ T ≤ 50
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # 10 ≤ N ≤ 100,  2 ≤ M ＜ N
    arr = list(map(int, input().split()))
    max_sum = 0
    min_sum = 10000 * M

    for i in range(N-M+1):
        num_sum = 0
        for j in range(M):
            num_sum += arr[i+j]
        if max_sum <= num_sum:
            max_sum = num_sum
        if min_sum >= num_sum:
            min_sum = num_sum

    result = max_sum - min_sum

    print(f'#{test_case} {result}')