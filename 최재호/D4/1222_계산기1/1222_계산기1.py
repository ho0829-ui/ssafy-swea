import sys
sys.stdin = open('input.txt', 'r')

def calc(cal):
    stack = []
    for item in cal:
        if item == '+':
            stack.append(item)
        else:
            stack.append(int(item))
            if len(stack) == 3:
                c = stack.pop()
                b = stack.pop()
                a = stack.pop()
                if b == '+':
                    stack.append(a+c)
    return stack.pop()

T = 10
for tc in range(1, T+1):
    n = int(input())
    cal = list(input().strip())

    print(f'#{tc} {calc(cal)}')