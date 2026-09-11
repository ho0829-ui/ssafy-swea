import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    binary = list(input().strip())
    ternary = list(input().strip())
    binary_to_decimal = set()
    ternary_to_decimal = set()

    for i in range(len(binary)):
        b_origin = binary[i] # 미리 바꾸고 싶은 자리 수 원본 저장
        if binary[i] == '0': # 2진수의 자리수가 0이면 1, 1이면 0으로 바꿔
            binary[i] = '1'
        else:
            binary[i] = '0'
        value = int(''.join(binary), 2) # 문자열을 숫자로 바꾸고 2진수로 만들어
        binary_to_decimal.add(value)
        binary[i] = b_origin # 다시 숫자를 원래대로 만들어

    for i in range(len(ternary)):
        t_origin = ternary[i]
        for digit in ('0', '1', '2'):
            if t_origin == digit: # 3진수 자리수가 바꿀 값이랑 같다면 바꿀 필요 없어 없어
                continue
            ternary[i] = digit # 자리수를 바꿔 바꿔
            value = int(''.join(ternary), 3) # 3진수를 만들어
            ternary_to_decimal.add(value)
            ternary[i] = t_origin # 다시 숫자를 원래대로 만들어

    print(f'#{tc}', end=' ')
    print(*(binary_to_decimal & ternary_to_decimal)) # 세트는 교집합 구하기 쉬움