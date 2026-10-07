import sys
sys.stdin = open('영준이와신비한뿔의숲.txt')

# n개의 뿔, m마리의 짐승
# cnt + twin_cnt = m
# cnt + 2*twin_cnt = n

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    twin_cnt = 0

    twin_cnt = N - M
    cnt = N - 2*twin_cnt
    print(f'#{tc} {cnt} {twin_cnt}')
