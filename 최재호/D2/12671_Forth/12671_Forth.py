import sys
sys.stdin = open('sample_input.txt', 'r')

def calc(cal):
    stack = []

    for item in cal:
        if item == '.':
            if len(stack) == 1:
                return stack.pop()
            return 'error'
        elif item in ['+', '-', '*', '/']:
            if len(stack) < 2:
                return 'error'
            b = stack.pop()
            a = stack.pop()
            if item == '+':
                result = a + b
            elif item == '-':
                result = a - b
            elif item == '*':
                result = a * b
            else:
                if b == 0:
                    return 'error'
                result = a // b
            stack.append(result)
        else:
            stack.append((int(item)))
    return 'error'



T = int(input())
for tc in range(1, T+1):
    cal = list(input().split())

    print(f'#{tc} {calc(cal)}')
