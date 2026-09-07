import sys
sys.stdin = open("sample_input.txt", "r")

def solve(data):
    # 검사할 문장의 시작점 순회
    for i in range(N): # 모든 행 검사
        for j in range(N-M+1): # 열은 M보다 작은 뒤쪽은 검사하지 않음
            # j 열에서 시작하는 길이 M 짜리 회문이 있는지 검사
            is_find = True
            for k in range(M//2):
                # j+k번이랑 j+M-1-k번이랑 비교
                if data[i][j+k] != data[i][j+M-1-k]:
                    is_find = False
                    break
            if is_find: # j번 부터 j+M-1번까지가 회문
                palindrome = ''
                for l in range(j,j+M):
                    palindrome += data[i][l]
                return palindrome

    for i in range(N): # 모든 행 검사
        for j in range(N-M+1): # 열은 M보다 작은 뒤쪽은 검사하지 않음
            # j 열에서 시작하는 길이 M 짜리 회문이 있는지 검사
            is_find = True
            for k in range(M//2):
                # j+k번이랑 j+M-1-k번이랑 비교
                if data[j+k][i] != data[j+M-1-k][i]:
                    is_find = False
                    break
            if is_find: # j번 부터 j+M-1번까지가 회문
                palindrome = ''
                for l in range(j,j+M):
                    palindrome += data[l][i]
                return palindrome

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input().strip() for _ in range(N)]

    result = solve(data)

    print(f'#{tc} {result}')

    # # 행 탐색
    # for i in range(N):
    #     is_okay = True
    #     for j in range(M//2):
    #         if text[i][j] != text[i][M-j-1]:
    #             is_okay = False
    #             break
    #     if is_okay == True:
    #         print(f'#{tc} {text[i]}')
    #
    # # 열 탐색
    # if is_okay == False:
    #     for j in range(M):
    #         is_okay = True
    #         for i in range(N//2):
    #             if text[i][j] != text[N-i-1][j]:
    #                 is_okay = False
    #                 break
    #         if is_okay == True:
    #             print(f'#{tc}', end=' ')
    #             print(*(text[k][j] for k in range(N)), sep='')
