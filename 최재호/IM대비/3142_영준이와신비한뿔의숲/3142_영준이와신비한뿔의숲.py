import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    T = N - M
    U = 2 * M - N

    print(f'#{tc} {U} {T}')