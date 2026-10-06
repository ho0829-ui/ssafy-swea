import sys
sys.stdin = open('test_in.txt', 'r')

def dfs(x):
    if x == e:
        return 1

    total = 0
    for y in graph[x]:
        if visited[y] == 1:
            continue
        visited[y] = 1
        total += dfs(y)
        visited[y] = 0
    return total


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    node = list(map(int, input().split()))
    s, e = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for i in range(E):
        graph[node[i*2]].append(node[i*2+1])

    visited = [0] * (N + 1)
    visited[s] = 1

    print(f'#{tc} {dfs(s)}')