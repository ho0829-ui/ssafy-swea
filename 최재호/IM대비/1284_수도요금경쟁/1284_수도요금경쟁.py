import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # A는 리터당 P원
    # B는 R이하 기본 Q원 초과 리터당 S원
    P, Q, R, S, W = map(int, input().split())

    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + (W-R) * S

    print(f'#{tc} {min(A, B)}')