import sys
sys.stdin = open('sample_input.txt', 'r')

def solve(idx, remain, cnt):
    global min_cnt

    if cnt >= min_cnt:
        return

    if idx == battery[0]:
        min_cnt = min(min_cnt, cnt)
        return

    # 배터리 교환하고 다음으로 이동
    solve(idx+1, battery[idx]-1, cnt+1)
    # 배터리 잔량이 남아 있을 때 배터리 교환하지 않고 다음으로 이동
    if remain > 0:
        solve(idx+1, remain-1, cnt)

T = int(input())
for tc in range(1, T+1):
    battery = list(map(int, input().split()))
    min_cnt = 100

    solve(2, battery[1] - 1, 0)

    print(f'#{tc} {min_cnt}')