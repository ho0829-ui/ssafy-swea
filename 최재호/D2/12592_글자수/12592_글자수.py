import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    unique_chars = set(str1)

    max_cnt = 0
    for char in unique_chars:
        cnt = 0
        for j in range(len(str2)):
            if char == str2[j]:
                cnt+=1
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')

