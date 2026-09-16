import sys
sys.stdin = open("GNS_test_input.txt", "r")
# T = int(input())
# for tc in range(1, T+1):
#     tc, n = input().split()
#     n = int(n)
#     arr = list(input().split())
#     num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     values = [num_lst.index(word) for word in arr]
#     sorted_words = [num_lst[v] for v in sorted(values)]
#     print(f'{tc}')
#     print(*sorted_words)

num_dict = {
'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9
}

def counting_sort(numbers):
    cnt = [0] * 10
    # numbers에 있는 문자열을 num_dict에 키 값으로 사용해 숫자를 뽑아 카운트 정렬하기 위한 cnt 리스트에 +1 추가
    for i in range(N):
        cnt[num_dict[numbers[i]]] += 1

    # 정렬하기 위해 인덱스를 사용할건데 누적합을 사용하여 각 마지막 인덱스를 알 수 있음
    for i in range(1, 10):
        cnt[i] += cnt[i-1]

    sorted_arr = [None] * N

    # 이제 numbers를 정렬하기 위해 numbers의 길이만큼 문자열 생성
    for i in range(N):
        cnt[num_dict[numbers[i]]] -= 1 # 인덱스는 0부터 시작하니 -1 해야함
        sorted_arr[cnt[num_dict[numbers[i]]]] = numbers[i]

    return sorted_arr

def buble_sort(numbers):
    for i in range(N-1):
        for j in range(N-1-i):
            if num_dict[numbers[j]] > num_dict[numbers[j+1]]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

        return numbers

T = int(input())
for tc in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    numbers = input().split()
    numbers = counting_sort(numbers)

    print(tc)
    print(*numbers)