import sys
sys.stdin = open('기차_사이의_파리.txt')

T = int(input())

for tc in range(1, T+1):
    # D: 두 기차 전면부 사이의 거리, A: 기차 A 속력, B: 기차 B 속력, F: 파리 속력
    D, A, B, F = map(int, input().split())  

    # A,B기차가 충돌하기까지 걸리는 시간
    collision_time = D / (A+B)   

    # 파리의 속력과 A,B 기차가 충돌하기까지 걸리는 시간을 곱하면 파리의 총 이동 거리가 나옴
    fly_distance = F * collision_time

    print(f'#{tc} {fly_distance}') 