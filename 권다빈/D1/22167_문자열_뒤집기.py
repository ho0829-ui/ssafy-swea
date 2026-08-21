# input
# 3
# hello
# python
# algorithm

# output
# olleh
# nohtyp
# mhtirogla

T = int(input())

for test_case in range(1, T + 1):
    word = input()
    print(word[::-1])