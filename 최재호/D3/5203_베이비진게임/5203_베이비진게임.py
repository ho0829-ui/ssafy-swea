import sys
sys.stdin = open('sample_input.txt', 'r')


def rrun(p):
    p = sorted(set(p))
    for i in range(len(p) - 2):
        if p[i] + 1 == p[i+1] and p[i] + 2 == p[i+2]:
            return True
    return False

def triplet(p):
    p.sort()
    for i in range(len(p) - 2):
        if p[i] == p[i+1] == p[i+2]:
            return True
    return False


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []

    result = 0

    for i in range(len(arr)):
        # player 1
        if i % 2 == 0:
            p1.append(arr[i])
            if len(p1) >= 3:
                if rrun(p1) or triplet(p1):
                    result = 1
                    break
        # player 2
        else:
            p2.append(arr[i])
            if len(p2) >= 3:
                if rrun(p2) or triplet(p2):
                    result = 2
                    break

    print(f'#{tc} {result}')

