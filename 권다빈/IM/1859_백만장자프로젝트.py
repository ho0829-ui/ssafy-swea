import sys
sys.stdin = open('1859_백만장자프로젝트.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    high_money = 0

    # 뒤에서부터 탐색해서 큰 값을 저장하고 그것보다 작으면 
    for i in range(len(arr)-1,-1,-1):
        if high_money < arr[i]:
            high_money = arr[i]
        else:   # 뒤에 날짜보다 값이 싼 의미이기 때문에 구매
            ans += high_money - arr[i]
    print(f'#{tc} {ans}')

        

