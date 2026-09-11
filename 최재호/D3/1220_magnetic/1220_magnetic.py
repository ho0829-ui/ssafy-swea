import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for column in zip(*board): # 열 탐색 : zip을 이용해 같은 열에 있는 요소를 튜플로 묶음
        prev = 0
        for value in column:
            if value == 0: # 요소가 0이면 신경 쓸 필요 없음
                continue
            if prev == 1 and value == 2: # 열에서 가장 위 2, 가장 아래 1은 필요 없음, 이전 값 1이고 현재가 2이면 교착 상태 완성, 이전에 1이거나 이후에 2가 붙으면 어쩌피 교착상태 유지라서 괜찮음
                answer += 1
            prev = value

    print(f'#{tc} {answer}')