import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    stack = []
    top = -1

    for i in range(len(str1)):
        stack.append(str1[i])
        top += 1
        if top >= 1 and stack[top-1] == stack[top]:
            stack.pop(top)
            stack.pop(top-1)
            top -= 2

    cnt = 0
    for i in range(len(stack)):
        cnt+=1

    print(f'#{tc} {cnt}')