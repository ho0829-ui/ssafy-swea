import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    while N > 0:
        max_box_index = boxes.index(max(boxes))
        min_box_index = boxes.index(min(boxes))

        boxes[min_box_index] += 1
        boxes[max_box_index] -= 1

        N -= 1

    max_b = max(boxes)
    min_b = min(boxes)

    print(f'#{tc} {max_b - min_b}')