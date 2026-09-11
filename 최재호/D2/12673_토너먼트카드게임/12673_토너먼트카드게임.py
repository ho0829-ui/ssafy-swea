import sys
sys.stdin = open('sample_input.txt', 'r')

def solve(start, end):
    if start == end:
        return start
    mid = (start+end)//2
    winner1 = solve(start, mid)
    winner2 = solve(mid+1,end)
    p1 = rsp[winner1]
    p2 = rsp[winner2]
    winner = winner1
    if p1 == 1 and p2 == 2:
        winner = winner2
    elif p1 == 2 and p2 == 3:
        winner = winner2
    elif p1 == 3 and p2 == 1:
        winner = winner2
    return winner

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rsp = [0] + list(map(int, input().split()))
    result = solve(1, N)
    print(f'#{tc} {result}')
