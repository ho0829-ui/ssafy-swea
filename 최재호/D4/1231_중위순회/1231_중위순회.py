import sys
sys.stdin = open('input.txt', 'r')

def in_order(T):
    if T:
        in_order(left[T])
        text.append(par[T])
        in_order(right[T])

T= 10
for tc in range(1, T+1):
    N = int(input())

    par = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        node = input().split()

        idx = int(node[0])
        par[idx] = node[1]

        if len(node) == 4:
            left[idx] = int(node[2])
            right[idx] = int(node[3])
        if len(node) == 3:
            left[idx] = int(node[2])

    root = 1
    text = []
    in_order(root)

    print(f'#{tc}', ''.join(text))
