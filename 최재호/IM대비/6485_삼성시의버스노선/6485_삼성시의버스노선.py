import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P_cnt = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            P_cnt[i] += 1

    P = int(input())
    P_station = [int(input()) for _ in range(P)]

    print(f'#{tc}', end=' ')
    for p in P_station:
        print(P_cnt[p], end=' ')
    print()