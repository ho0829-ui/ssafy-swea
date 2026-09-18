import sys
sys.stdin = open('sample_input.txt', 'r')

def f(t):
    global cnt
    if t <= N:
        f(t * 2)
        cnt += 1
        tree[t] = cnt
        f(t * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N + 1)
    cnt = 0
    f(1)