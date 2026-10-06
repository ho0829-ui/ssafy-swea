import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    if arr[0] == arr[1]:
        print(f'#{tc} {arr[2]}')
    elif arr[0] == arr[2]:
        print(f'#{tc} {arr[1]}')
    elif arr[1] == arr[2]:
        print(f'#{tc} {arr[0]}')