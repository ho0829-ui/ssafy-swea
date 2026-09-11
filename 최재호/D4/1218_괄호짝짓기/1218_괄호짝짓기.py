import sys
sys.stdin = open('input.txt', 'r')
T = 10
for tc in range(1, T+1):
    n = int(input())
    text = input()
    pair = ['(', ')', '[', ']', '{', '{', '<', '>']
    stack = []
    top = -1

    for i in range(n):
        stack.append(text[i])
        top += 1
        if top >= 1 and stack[top-1] == '(' and stack[top] == ')':
            stack.pop(top)
            stack.pop(top-1)
            top -= 2
        elif top >= 1 and stack[top-1] == '[' and stack[top] == ']':
            stack.pop(top)
            stack.pop(top-1)
            top -= 2
        elif top >= 1 and stack[top-1] == '{' and stack[top] == '}':
            stack.pop(top)
            stack.pop(top-1)
            top -= 2
        elif top >= 1 and stack[top-1] == '<' and stack[top] == '>':
            stack.pop(top)
            stack.pop(top-1)
            top -= 2

    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')