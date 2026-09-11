import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    return dfs(n - 10) + 2 * dfs(n - 20)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    result = dfs(n)

    print(f'#{tc} {result}')