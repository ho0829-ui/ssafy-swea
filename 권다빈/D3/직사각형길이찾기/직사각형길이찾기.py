import sys
sys.stdin = open('직사각형길이찾기.txt')

T = int(input())

for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    if a == b:
        print(f'#{tc} {c}')
    elif a == c:
        print(f'#{tc} {b}')
    else:
        print(f'#{tc} {a}')