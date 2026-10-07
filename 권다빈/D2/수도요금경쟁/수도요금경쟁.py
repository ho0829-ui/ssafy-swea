import sys
sys.stdin = open('수도요금경쟁.txt')

T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    # A사의 한달 요금
    A_cost = P * W
    
    # B사의 한달 요금
    # R 기준으로 계산
    if W <= R:
        B_cost = Q
    else:
        B_cost = Q + ((W-R)*S)

    print(f'#{tc} {min(A_cost, B_cost)}')