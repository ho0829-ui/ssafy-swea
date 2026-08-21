T = int(input())

for test_case in range(1, T + 1):
    t = int(input())
    scores = list(map(int, input().split()))
    count_score = {}
    max_count = 0
    max_score = 0

    for score in scores:
        count_score[score] = count_score.get(score, 0) + 1

    for value in count_score.values():
        if value > max_count:
            max_count = value

    for key, value in count_score.items():
        if value == max_count:
            if max_score <= key:
                max_score = key
    print(max_score)