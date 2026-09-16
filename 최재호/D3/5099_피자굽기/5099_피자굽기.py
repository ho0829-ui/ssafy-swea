import sys
sys.stdin = open('sample_input.txt', 'r')

def oven(pizza):
    q = []
    # 처음 N개 피자 화덕에 넣기
    for i in range(N):
        q.append(pizza[i])

    # 다음에 올 피자 인덱스
    next_pizza = N

    # 마지막 피자가 남을 때 까지
    while len(q) > 1:
        C = q.pop(0)
        C[1] //= 2
        if C[1] != 0:
            q.append(C)
        else:
            if next_pizza < M:
                q.append(pizza[next_pizza])
                next_pizza += 1

    return q[0][0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    pizza = []

    for i in range(M):
        pizza.append([i+1, Ci[i]])

    result = oven(pizza)

    print(f'#{tc} {result}')