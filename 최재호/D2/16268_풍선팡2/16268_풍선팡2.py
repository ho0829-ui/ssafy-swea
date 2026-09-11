import sys
sys.stdin = open('input1.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_n = 0

    # 풍선이 터지면 풍선 터진 자리에서 상 하 좌 우 를 탐색하기
    for r in range(n):
        for c in range(m):
            sum_delta = arr[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m: # 배열 범위 안에 있다면 꽃가루 합치기
                    sum_delta += arr[nr][nc]
            if max_n < sum_delta:
                max_n = sum_delta

    print(f'#{tc} {max_n}')

# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     sum_lst = []
#
#     for r in range(n):
#         for c in range(m):
#             sum_delta = arr[r][c]
#             for d in range(4):
#                 nr, nc = r+delta[d][0], c+delta[d][1]
#                 if 0 <= nr < n and  0 <= nc < m:
#                     sum_delta += arr[nr][nc]
#             sum_lst.append(sum_delta)
#
#     max_n = sum_lst[0]
#     for i in range(len(sum_lst)-1):
#         if max_n < sum_lst[i]:
#             max_n = sum_lst[i]
#
#     print(f'#{tc} {max_n}')