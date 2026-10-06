import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_num = 100001
    cnt = 0

    for i in range(N):
        if min_num > abs(arr[i]):
            min_num = abs(arr[i])
            cnt = 1
        elif min_num == abs(arr[i]):
            cnt += 1
    print(f'#{tc} {min_num} {cnt}')