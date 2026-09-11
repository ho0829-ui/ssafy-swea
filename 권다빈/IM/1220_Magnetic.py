import sys
sys.stdin = open('1220_Magnetic.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0  # 교착상태 저장할 변수

    # N:1, S:2
    # 1은 i가 큰쪽에 있으면 없어지고, 2는 i가 작은 쪽에 있으면 없어짐
    for j in range(N):
        flag = False
        for i in range(N):
            if arr[i][j] == 1:
                flag = True
            elif arr[i][j] == 2:
                # 1과2가 교착상태이기 때문에 ans카운팅
                if flag:
                    ans += 1
                    flag = False
    print(f'#{tc} {ans}')

