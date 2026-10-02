import sys
sys.stdin = open('input.txt', 'r')

def find_max_award(cnt):
    global result

    state = (cnt, ''.join(award_lst))

    if state in visited:
        return

    visited.add(state)

    if cnt == suffle: # 숫자 교환을 다 하면
        num = int(''.join(award_lst))
        result = max(result, num) # 최대값을 결과값에 넣기
        return

    for i in range(award_len-1):
        for j in range(i+1, award_len):
            award_lst[i], award_lst[j] = award_lst[j], award_lst[i]

            find_max_award(cnt+1)

            # 복구
            award_lst[i], award_lst[j] = award_lst[j], award_lst[i]

T = int(input())
for tc in range(1, T+1):
    award, suffle = input().split()

    award_lst = list(award)
    award_len = len(award)
    suffle = int(suffle)

    result = 0
    visited = set()

    find_max_award(0)

    print(f'#{tc} {result}')