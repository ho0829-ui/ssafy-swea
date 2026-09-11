import sys
sys.stdin = open("sample_input.txt", "r")

# for i in range(1, 11):
#     N = int(input()) # 4 ≤ N ≤ 1000
#     buildings = list(map(int, input().split())) # 0 ≤ 각 건물의 높이 ≤ 255
#     max_h = 0
#
#     for j in range(2, N-2):
#         if all(buildings[j] - buildings[j+d] >= 1 for d in (-2, -1, 1, 2)):
#             max_h += buildings[j] - max(buildings[j - 2], buildings[j - 1], buildings[j + 1], buildings[j + 2])
#
#     result = max_h
#     print(f'#{i} {result}')


for i in range(1, 11):
    N = int(input()) # 4 ≤ N ≤ 1000
    buildings = list(map(int, input().split())) # 0 ≤ 각 건물의 높이 ≤ 255
    max_h = 0

    for j in range(2, N-2):
        tall = buildings[j-2]
        for c in (-1,1,2):
            if buildings[j+c] > tall:
                tall = buildings[j+c]
        gap = buildings[j] - tall
        if gap >= 1:
            max_h += gap

    result = max_h
    print(f'#{i} {result}')
