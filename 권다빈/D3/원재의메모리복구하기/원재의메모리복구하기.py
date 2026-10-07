import sys
sys.stdin = open('원재의메모리복구하기.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    tmp = ['0'] * len(arr)
    ans = 0

    for i in range(len(arr)):
        if arr[i] != tmp[i]:
            ans += 1
            for j in range(i, len(arr)):
                tmp[j] = arr[i]
    print(f'#{tc} {ans}')