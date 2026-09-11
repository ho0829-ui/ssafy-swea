import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []
    top = -1

    for i in range(len(text)):
        if text[i] in ['(', ')', '{', '}']:
            stack.append(text[i])
            top += 1
        if top >= 1 and stack[top-1] == '{' and stack[top] == '}':
            stack.pop(top)
            stack.pop(top-1)
            top -= 2
        elif top >= 1 and stack[top-1] == '(' and stack[top] == ')':
            stack.pop(top)
            stack.pop(top-1)
            top -= 2

    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')