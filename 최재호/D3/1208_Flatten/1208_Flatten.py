import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1,T+1):
    dump_count = int(input())
    blocks = list(map(int, input().split()))

    while dump_count > 0:
        max_idx = 0
        min_idx = 0
        for i in range(len(blocks)):
            if blocks[max_idx] < blocks[i]:
                max_idx = i
            if blocks[min_idx] > blocks[i]:
                min_idx = i

        if blocks[max_idx] - blocks[min_idx] <= 1:
            break

        blocks[max_idx] -= 1
        blocks[min_idx] += 1

        dump_count -= 1

    print(f'#{test_case} {max(blocks)-min(blocks)}')
