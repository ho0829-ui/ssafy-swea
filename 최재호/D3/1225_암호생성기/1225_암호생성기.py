import sys
sys.stdin = open('input.txt', 'r')

def mq(password):
    # q 생성
    q = password[:]

    inc = 1

    while True:
        t = q.pop(0)
        t -= inc

        if t <= 0:
            q.append(0)
            return q

        q.append(t) # 맨뒤로 이동
        inc += 1
        if inc > 5:
            inc = 1


T = 10
for tc in range(1, T+1):
    tc = int(input())
    password = list(map(int, input().split()))

    result = mq(password)

    print(f'#{tc}', *result)