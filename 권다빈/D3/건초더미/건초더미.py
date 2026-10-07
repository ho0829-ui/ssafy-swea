import sys
sys.stdin = open('건초더미.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        si = int(input())
        arr.append(si)
    
    mid = sum(arr)//len(arr)
    ans = 0
    for i in range(N):
        ans += abs(mid - arr[i])

    print(f'#{tc} {ans//2}')
