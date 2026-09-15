import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    electric_wire = [list(map(int, input().split())) for _ in range(N)]

    electric_wire.sort()
    cnt = 0
    for i in range(1, N):
        for j in range(i):
            if electric_wire[j][1] > electric_wire[i][1]:
                cnt += 1
    print(f'#{tc} {cnt}')
