import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())

    min_sub = max(0, A+B-N)

    max_sub = min(A, B)

    print(f'#{tc} {max_sub} {min_sub}')