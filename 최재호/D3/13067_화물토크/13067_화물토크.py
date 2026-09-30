import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trucks = []

    result = 0

    for _ in range(N):
        s, e = map(int, input().split())
        trucks.append((s, e))

    trucks.sort(key=lambda x: x[1]) # 종료시간이 빠른 순서대로 정렬

    result = 0
    end_time = 0

    for s, e in trucks:
        if s >= end_time:
            result += 1
            end_time = e


    print(f'#{tc} {result}')