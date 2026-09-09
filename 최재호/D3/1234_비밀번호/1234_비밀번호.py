import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1,T+1):
    n, str1 = input().split()
    n = int(n)
    str1 = list(str1)
    password = []
    password.append(str1[0])
    top = 0

    for i in range(1, len(str1)):
        password.append(str1[i])
        top += 1
        if top >= 1 and password[top-1] == password[top]:
            password.pop(top)
            password.pop(top-1)
            top -= 2
    password = ''.join(password)

    print(f'#{tc} {password}')