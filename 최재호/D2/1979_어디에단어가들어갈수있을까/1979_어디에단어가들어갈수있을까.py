import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    total_cnt = 0

    for row in puzzle: # 행 탐색
        cnt = 0
        for box in row:
            if box == 1: # 박스 1칸이 1이면
                cnt += 1 # 카운트하기
            else:        # 0을 만나면
                if cnt == K: # 현재까지 쌓아온 카운트가 K개 일때 K길이의 단어를 만들 수 있기 때문에 진짜 카운트
                    total_cnt += 1
                cnt = 0 # 하지만 1인 값 K개만큼 연속으로 있지 않은 경우 단어 카운트는 처음부터
        if cnt == K: # 행 을 다 순회해서 K개 만큼 이어져 있다면 카운트 하기
            total_cnt += 1

    for column in zip(*puzzle): # 열 탐색(행이랑 동일한 구조)
        cnt = 0
        for item in column:
            if item == 1:
                cnt += 1
            else:
                if cnt == K:
                    total_cnt += 1
                cnt = 0
        if cnt == K:
            total_cnt += 1

    print(f'#{tc} {total_cnt}')