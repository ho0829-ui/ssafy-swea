import sys
sys.stdin = open('아름이의돌던지기.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 돌이 떨어진 위치
    arr = list(map(int, input().split()))
    
    pos = 0
    nearest_pos = float('inf')
    cnt = 0
    for i in range(N):
        if abs(arr[i]) < nearest_pos:
            nearest_pos = abs(arr[i])

    for i in range(N):
        if abs(arr[i]) == nearest_pos:
            cnt += 1
    print(f'#{tc} {nearest_pos} {cnt}')
