import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
dic = {}

for i in range(N):
    str_i = str(arr[i])
    if str_i not in dic:  # 키에 str_i이 없다면 str 형태인 키추가하면서 value에 1 추가
        dic[str(arr[i])] = 1
    else: # 만약 있다면 그냥 value에 +1
        dic[str(arr[i])] += 1

for k, v in dic.items():
    print(k, v)