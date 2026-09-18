import sys
sys.stdin = open('sample_input.txt', 'r')

T= int(input())
for tc in range(1, T+1):
    N = float(input())

    bin_num = ''
    for _ in range(12):
        N *= 2

        if N >= 1:
            bin_num += '1'
            N -= 1
        else:
            bin_num += '0'

        if N == 0:
            break
    else:
        print(f'#{tc} overflow')
        continue

    print(f'#{tc} {bin_num}')