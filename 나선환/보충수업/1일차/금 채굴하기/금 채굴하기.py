n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for y in range(n):
    for x in range(n):

        for k in range(2 * n - 1):
            cnt = 0

            for i in range(n):
                for j in range(n):

                    if abs(y - i) + abs(x - j) <= k:
                        if grid[i][j] == 1:
                            cnt += 1

            cost = k * k + (k + 1) * (k + 1)

            if cnt * m >= cost:
                ans = max(ans, cnt)

print(ans)
