import sys
sys.stdin = open('sample_input.txt', 'r')
import heapq

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, l = map(int, input().split())
        adj[s].append((e, l))

    INF = float('inf')
    dist = [INF] * (N+1)
    dist[0] = 0
    pq = [(0, 0)]

    while pq:
        cur_len, c = heapq.heappop(pq)

        if cur_len > dist[c]:
            continue

        for n, length in adj[c]:
            new_len = cur_len + length
            if new_len < dist[n]:
                dist[n] = new_len
                heapq.heappush(pq, (new_len, n))

    print(f'#{tc} {dist[N]}')