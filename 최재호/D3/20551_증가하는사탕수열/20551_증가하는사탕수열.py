import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    # candy[2]가 3미만이면 아무리 먹어도 만족시킬 수 없다.
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