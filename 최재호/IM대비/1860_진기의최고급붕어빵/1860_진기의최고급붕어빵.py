import sys
sys.stdin = open('input.txt', 'r')

# def solve():
#     b = 0
#
#     for i in range(0, max_vt+1):
#         if i != 0 and i % M == 0:
#             b += K
#
#         if i in vt:
#             count_i = vt.count(i)
#             b -= count_i
#             if b < 0:
#                 return 'Impossible'
#
#     if b >= 0:
#         return 'Possible'
#
# T = int(input())
# for tc in range(1, T+1):
#     # N명의 사람, M초 걸리면 K개 붕어빵
#     N, M, K = map(int, input().split())
#     vt = list(map(int, input().split()))
#     vt.sort()
#     max_vt = max(vt)
#
#     result = solve()
#
#     print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T+1):
    # N명의 사람, M초 걸리면 K개 붕어빵
    N, M, K = map(int, input().split())
    vt = list(map(int, input().split()))
    vt.sort()
    result = None

    for idx, t in enumerate(vt):
        b = (t//M) * K
        c = idx + 1

        if b < c:
            result = 'Impossible'
            break
    else:
        result = 'Possible'

    print(f'#{tc} {result}')