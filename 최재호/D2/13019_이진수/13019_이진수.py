import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()

    bin_num = ''
    for i in range(int(N)):
        dec_num = int(hex_num[i], 16)
        bin_num += format(dec_num, '04b')

    print(f'#{tc} {bin_num}')