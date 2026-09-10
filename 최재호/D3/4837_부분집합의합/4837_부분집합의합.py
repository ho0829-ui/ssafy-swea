import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(N, K):
    stack = []
    visited = [0]*13
    sum_n = 0
    cnt = 0
    for i in range (1, N+1):
        stack.append(i)
        visited[i] = 1
        sum_n += i
        if sum_n == K:

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(13)]

    result = dfs(N, K)

    print(f'{tc} {result}')