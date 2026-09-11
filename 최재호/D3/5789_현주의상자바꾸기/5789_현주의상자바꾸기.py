import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]

    boxes = [0] * (N+1) # boxes의 인덱스를 접근해서 값을 넣기

    for i in range(1, Q+1):
        start, end = arr[i-1][0], arr[i-1][1] # start와 end 범위를 설정해서 반복문 사용하면 범위의 인덱스에 i 값 들어감
        for num in range(start, end+1):
            boxes[num] = i

    print(f'#{tc}', *boxes[1:])