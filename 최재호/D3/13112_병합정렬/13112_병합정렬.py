import sys
sys.stdin = open('sample_input.txt', 'r')


def mergeSort(s, e):
    global cnt

    if s == e:
        return

    mid = s + (e - s + 1) // 2

    mergeSort(s, mid - 1)
    mergeSort(mid, e)

    if arr[mid - 1] > arr[e]:
        cnt += 1

    sorted_arr = []

    i = s
    j = mid

    while i < mid and j <= e:
        if arr[i] <= arr[j]:
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1

    while i < mid:
        sorted_arr.append(arr[i])
        i += 1

    while j <= e:
        sorted_arr.append(arr[j])
        j += 1

    b = 0
    for x in range(s, e + 1):
        arr[x] = sorted_arr[b]
        b += 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0

    mergeSort(0, N - 1)

    print(f'#{tc} {arr[N // 2]} {cnt}')