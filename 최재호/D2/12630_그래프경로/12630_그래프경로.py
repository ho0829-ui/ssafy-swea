import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(start, end):
    stack = []
    stack.append(start)
    visited = [0] * (V+1)
    visited[start] = 1

    while stack:
        current = stack[-1]
        for v in range(1, V+1):
            if adj[current][v] and visited[v] == 0:
                stack.append(v)
                visited[v] = 1
                if visited[end] == 1:
                    return 1
                break
        else:
            stack.pop()

    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj = [[0]*(V+1) for _ in range(V+1)]

    for i in range(0, E):
        s = edges[i][0]
        e = edges[i][1]
        adj[s][e] = 1

    result = dfs(S, G)

    print(f'#{tc} {result}')