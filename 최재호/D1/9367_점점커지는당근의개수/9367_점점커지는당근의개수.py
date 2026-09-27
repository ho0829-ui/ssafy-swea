import sys
sys.stdin = open('carrot_sample_in.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    # 우선 카운트는 1에서 시작
    cnt = 1
    max_cnt = 0
    # N의 범위를 순회하면서
    for i in range(1, N): # 0번 인덱스 이전 값을 볼 수 없으니 1부터 시작
        # i라면 i-1을 확인 후 만약 크기가 작다면 당근 카운트 +1
        if carrots[i] > carrots[i-1]:
            cnt += 1
        # 만약 이전 당근이 더 크다면 지금까지 카운트한 값을 최대 카운트에 저장 후
        else:
            # 카운트는 다시 1에서 시작
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    print(f'#{tc} {max_cnt}')