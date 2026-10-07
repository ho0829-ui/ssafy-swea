import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().strip()))

    app = 0
    result = 0

    for idx, a in enumerate(A):
        if app < idx:
            need = idx - app
            result += need
            app += need
        app += a

    print(f'#{tc} {result}')