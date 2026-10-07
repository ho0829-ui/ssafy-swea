import sys
sys.stdin = open('구독자전쟁.txt')

T = int(input())

for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    max_ppl = 0
    min_ppl = 0

    if A + B < N:
        max_ppl = min(A, B)
        min_ppl = 0
    else:
        max_ppl = min(A, B)
        min_ppl = A+B-N

    print(f'#{tc} {max_ppl} {min_ppl}')