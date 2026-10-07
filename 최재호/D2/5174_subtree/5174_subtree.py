import sys
sys.stdin = open('sample_input.txt', 'r')

def pre_order(T):
    global cnt
    if T:
        cnt += 1
        pre_order(left[T])
        pre_order(right[T])

def f(T):
    if T == 0: # 없는 정점이면
        return 0 # 방문한 개수는 0개
    # l은 왼쪽 서브트리의 정점 개수
    # r은 오른쪽 서브트리의 정점 개수
    l = f(left[T]) # 왼쪽 서브트리로 이동
    r = f(right[T]) # 오른쪽 서브트리로 이동
    return l + r + 1

T = int(input())
for tc in range(1, T+1):
    # 간선의 개수 E, 서브 트리 루트 N
    E, N = map(int, input().split())
    V = E + 1 # 마지막 정점 번호

    arr = list(map(int, input().split()))

    # 부모를 인덱스로 자식 번호 저장
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    pre_order(N)

    print(f'{tc} {cnt}')
