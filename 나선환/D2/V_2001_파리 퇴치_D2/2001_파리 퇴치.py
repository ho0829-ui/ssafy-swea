import sys
sys.stdin = open("input.txt", "r")

"""
문제 구상
방 안에 영역으로 나눠져있고 그 영역에 각각 파리들이 있음
파리채로 파리를 잡으려고함
파리채로 구역을 한번 내리칠 때 가장 많이 죽인 파리수를 구하기

로직 구상
1. 가로x세로 영역을 2차원 리스트로 만듬 # 2차원 리스트
2. 파리채의 크기를 2중 for문으로 구한다음 거기에 해당되는 파리 수를 전부 더함
3. 모든 구역을 돌아가면서 가장 많이 죽인 파리수를 구하기
4. 가장 많이 죽인 파리수를 테스트케이스와 함께 출력
"""

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # 1. 가로x세로 영역을 2차원 리스트로 만들기 # 2차원 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 3. 모든 구역을 돌아가면서 가장 많이 죽인 파리수를 구하기
    # 3-2. 가장 많이 죽인 파리수 초기값 세팅
    max_count = 0
    # 3-1. 모든 구역을 돌아가면서 파리채 휘두르기
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 2. 파리채의 크기를 2중 for문으로 구한다음 거기에 해당되는 파리수를 전부 더함
            # 2-2. 파리채로 잡은 파리수를 더할 초기값 세팅
            count = 0
            # 2-1. 파리채의 크기를 2중 for문으로 구함(파리채의 시작은 i, j부터 시작해야함)
            for mi in range(i, i + M):
                for mj in range(j, j + M):
                    # 2-3. 파리채로 잡은 파리수를 전부 더함
                    count += arr[mi][mj]
            # 3-3. 파리채로 잡은 파리수가 가장 많이 죽인 파리수의 개수보다 크다면 재할당
            if count > max_count:
                max_count = count
    # 4. 가장 많이 죽인 파리수를 테스트케이스와 함께 출력
    print(f"#{test_case} {max_count}")


