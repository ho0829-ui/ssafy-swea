import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))

    total_mean = sum(arr) // N

    cnt = 0
    for i in range(N):
        if arr[i] < total_mean:
            cnt += total_mean - arr[i]

    print(f'#{tc} {cnt}')