import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_sales = 0
    max_price = arr[-1]

    for i in range(n-2, -1, -1): # 가장 먼 미래부터 볼 거야
        if arr[i] > max_price: # 미래를 봤는데 과거의 값이 미래가 더 큰 경우 하나 큰 미래로 max_price 변경
            max_price = arr[i]
        else: # 만약 max_price가 더 크다면 max_price에서 구매한 가격을 뺴서 total에 더함
            sum_sales += max_price - arr[i]
    print(f'#{tc} {sum_sales}')