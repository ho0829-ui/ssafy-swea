import sys
sys.stdin = open('2805_농작물_수확하기.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    mid = N//2

    for i in range(N):
        if i <= mid:
            start = mid - i
            end = mid + i
        else:
            start = i - mid
            end = N-1 - (i-mid)

        for j in range(start, end+1):
            ans += arr[i][j]
    print(f'#{tc} {ans}')


