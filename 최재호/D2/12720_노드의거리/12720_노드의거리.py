import sys
sys.stdin = open('sample_input.txt', 'r')

def my_que(S, G):
    # 초기화
    # visited 생성
    visited = [0] * (V+1)
    # 큐 생성
    # 시작점 인큐
    q = [S]
    visited[S] = 1

    while q:
        t = q.pop(0)
        for w in adj[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
                if w == G:
                    return visited[w] - 1
    return 0

T = int(input())
for tc in range(1, T+1):
    # V개의 노드, E개 간선
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj = [[] for _ in range(V+1)]

    for i, j in node:
        adj[i].append(j)
        adj[j].append(i)

    result = my_que(S, G)

    print(f'#{tc} {result}')