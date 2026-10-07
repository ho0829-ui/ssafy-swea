import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    now = '0'
    cnt = 0

    for i in range(len(arr)):
        if arr[i] != now:
            cnt += 1
            now = arr[i]


    print(f'#{tc} {cnt}')
