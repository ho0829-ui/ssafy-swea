import sys
sys.stdin = open("GNS_test_input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    tc, n = input().split()
    n = int(n)
    arr = list(input().split())
    num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    values = [num_lst.index(word) for word in arr]
    sorted_words = [num_lst[v] for v in sorted(values)]
    print(f'{tc}')
    print(*sorted_words)