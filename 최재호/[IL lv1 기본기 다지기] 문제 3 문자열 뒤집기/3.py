import sys
sys.stdin = open("input.txt", "r")

T = int(input())
arr = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(T):
    arr.append(input())

new_arr = []
for i in range(T):
    reversed_text = "" # 빈 문자열 생성
    for j in range(len(arr[i])):
        reversed_text = arr[i][j] + reversed_text # "h" + "" 다음에 "e" + "h" 다음에 "l" + "eh"
    new_arr.append(reversed_text)

for i in range(T):
    print(new_arr[i])