import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1, str2 = input().split()
    i = 0
    cnt = 0
    while i <= len(str1) - len(str2):
        if str1[i:i+len(str2)] == str2:
            cnt += 1
            i += len(str2)
        else:
            i += 1

    result = len(str1) - (len(str2) * cnt) + cnt

    print(f'#{tc} {result}')