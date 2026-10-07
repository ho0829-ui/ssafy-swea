import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input()) # 정점의 개수 N

    tree = [None] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        n = input().split()

        idx = int(n[0])
        tree[idx] = n[1]

        if len(n) == 4:
            left[idx] = int(n[2])
            right[idx] = int(n[3])

    for i in range(N, 0, -1):
        if tree[i] == '-':
            tree[i] = int(tree[left[i]]) - int(tree[right[i]])
        elif tree[i] == '+':
            tree[i] = int(tree[left[i]]) + int(tree[right[i]])
        elif tree[i] == '*':
            tree[i] = int(tree[left[i]]) * int(tree[right[i]])
        elif tree[i] == '/':
            tree[i] = int(tree[left[i]]) // int(tree[right[i]])

    print(f'{tc} {tree[1]}')

