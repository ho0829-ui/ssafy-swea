import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input()) # 1 ≤ T ≤ 50
for test_case in range(1, T + 1):
    N = int(input()) # 5 ≤ N ≤ 100
    cnt = [0] * 10  # 0 ≤ ai ≤ 9
    arr = input()
    lst = []
    for i in range(N):
        lst.append(int(arr[i]))

    for j in range(N):
        cnt[lst[j]] += 1

    max_cnt = 0
    max_k = 0
    for k in range(10):
        if cnt[k] >= max_cnt:
            max_cnt = cnt[k]
            max_k = k

    print(f'#{test_case} {max_k} {max_cnt}')
