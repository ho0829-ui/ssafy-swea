import sys
sys.stdin = open('진기의최고급붕어빵.txt')

T = int(input())

for tc in range(1, T+1):
    # K: 붕어빵 개수
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    possible = True
    for i in range(N):
        total_bread = (arr[i]//M) * K

        # 총 붕어빵 수가 사람 수보다 적으면 impossible
        if total_bread < i+1:
            possible = False
            break

    if possible:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
