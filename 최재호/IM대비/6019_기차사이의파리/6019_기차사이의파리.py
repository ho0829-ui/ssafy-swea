import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # D 두 기차 전면부 사이의 거리
    # A A기차의 속력
    # B B기차의 속력
    # F 파리의 속력
    D, A, B, F = map(int, input().split())

    # 파리가 A전면부에서 날라가다가 B전면부에 부딪치면 방향 전환
    # 그러다가 A랑 B가 충돌하면 파리는 죽을 텐데
    # 그때 파리가 이동한 거리는??

    # 그렇다면 얼마만에 충돌하는가?
    conflict_time = D / (A + B)
    F_len = F * conflict_time

    print(f'#{tc} {F_len:.10f}')
