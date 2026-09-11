import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1):
        max_idx = i
        # min_idx = i
        for j in range(i, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
            # if arr[i] > arr[min_idx]:
            #     min_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    result = [0]*n
    for i in range(0, (n//2)):
        result[i*2], result[(i*2)+1] = arr[i], arr[n-i-1]
    result = result[:10]
    print(f'#{tc}', *result)