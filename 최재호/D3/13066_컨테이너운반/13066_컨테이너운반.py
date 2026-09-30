import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N : 컨테이너 수
    # M : 트럭 수
    N, M = map(int, input().split())

    w = list(map(int, input().split())) # 화물 무게
    w.sort(reverse=T)
    t = list(map(int, input().split())) # 트럭의 적재 용량
    t.sort(reverse=T)

    w_idx = 0
    t_idx = 0
    w_sum = 0

    while w_idx < N and t_idx < M:
        if t[t_idx] >= w[w_idx]:
            # 트럭에 현재 컨테이너 실을 수 있음
            w_sum += w[w_idx]
            t_idx += 1
            w_idx += 1
        else:
            # 컨테이너가 너무 무거움
            w_idx += 1

    print(f'#{tc} {w_sum}')