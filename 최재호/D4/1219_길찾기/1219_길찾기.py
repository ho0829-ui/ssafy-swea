import sys
sys.stdin = open('input.txt', 'r')

def dfs(s):
    if s == 99:
        return 1

    visited[s] = 1

    if adj_1[s] != 0 and not visited[adj_1[s]]:
        result = dfs(adj_1[s])

        if result ==1:
            return 1
    if adj_2[s] != 0 and not visited[adj_2[s]]:
        result = dfs(adj_2[s])

        if result == 1:
            return 1
    return 0

T = 10
for tc in range(1, T+1):
    tc, n = map(int, input().split())
    node = list(map(int, input().split()))
    adj_1 = [0] * 100
    adj_2 = [0] * 100

    for i in range(0, n*2, 4):
        adj_1[node[i]] = node[i+1]
    for j in range(2, n*2, 4):
        adj_2[node[j]] = node[j+1]

    visited = [0] * 100
    result = dfs(0)

    print(f'#{tc} {result}')