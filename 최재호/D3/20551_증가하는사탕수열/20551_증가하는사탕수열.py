import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    # 그리디 알고리즘 사용
    # 그리디 알고리즘 : 매 순간 지금에서 가장 좋아 보이는 방식을 선택
    # 한번 선택하고 뒤로 돌아가지 않음
    # 지금 당장 할 수 있는 최선을 선택함
    if A < 1 or B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    eat = 0
    if B >= C:
        eat += B - (C - 1)
        B = C - 1

    if A >= B:
        eat += A - (B - 1)
        A = B - 1

    print(f'#{tc} {eat}')