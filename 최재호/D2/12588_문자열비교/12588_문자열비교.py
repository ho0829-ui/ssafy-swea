import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = 0
    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)):
            if str2[i+j] != str1[j]:
                break
        else:
            cnt+=1
    print(f'#{tc} {cnt}')