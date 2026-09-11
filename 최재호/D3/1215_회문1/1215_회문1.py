import sys
sys.stdin = open("input.txt", "r")
T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [input().strip() for _ in range(8)]

    ans = 0

    for i in range(8):
        for j in range(8-n+1):
            for k in range(n//2):
                if arr[i][j+k] != arr[i][j+n-1-k]:
                    break
            else:
                ans += 1

    for i in range(8):
        for j in range(8-n+1):
            for k in range(n//2):
                if arr[j+k][i] != arr[j+n-1-k][i]:
                    break
            else:
                ans += 1

    print(f'#{tc} {ans}')