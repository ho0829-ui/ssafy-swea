import sys
sys.stdin = open('쥬스_나누기.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}', end=' ')
    for i in range(1, N+1):
        print(f'1/{N}', end=' ')
    print()
