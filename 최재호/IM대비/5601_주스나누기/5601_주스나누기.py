import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}', end=' ')
    print(f'1/{N} '*N, end='\n')