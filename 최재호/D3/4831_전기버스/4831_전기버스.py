import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    car_locaion = 0
    charging_cnt = 0

    stations = [0] * (N+1)
    for i in chargers:
        stations[i] = 1

    while car_locaion + K < N:
        finding_station = False
        for next in range(car_locaion+K,car_locaion,-1):
            if stations[next]==1:
                charging_cnt += 1
                car_locaion = next
                finding_station =True
                break
        if finding_station == False:
            charging_cnt = 0
            break

    print(f'#{test_case} {charging_cnt}')