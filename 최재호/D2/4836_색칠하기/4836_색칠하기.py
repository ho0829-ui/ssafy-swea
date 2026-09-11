import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    boxs = int(input())
    arr = [list(map(int, input().split())) for _ in range(boxs)]
    matrix = [[0]*10 for _ in range(10)]

    # arr 순회하면서 할당된 박스에 숫자 담을 준비
    # 같은 색 박스는 겹치지 않기 때문에 별다른 조건 필요없이 박스 범위만큼 +color 하기
    for k in range(boxs):
        a, b, c, d, e = arr[k][0], arr[k][1], arr[k][2], arr[k][3], arr[k][4]
        for i in range(a, c+1):
            for j in range(b, d+1):
                matrix[i][j] += e

    # matrix에 담긴 값이 2이면 박스가 겹쳤다는 뜻, count해서 결과 출력하기
    cnt = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
