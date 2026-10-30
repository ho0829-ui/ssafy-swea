n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for y in range(n):
    cnt = 1

    for x in range(1, n):
        if grid[y][x] == grid[y][x-1]:
            cnt += 1
        else:
            cnt = 1

        if cnt >= m:
            break

    if cnt >= m:
        ans += 1

for x in range(n):
    cnt = 1

    for y in range(1, n):
        if grid[y][x] == grid[y-1][x]:
            cnt += 1
        else:
            cnt = 1

        if cnt >= m:
            break

    if cnt >= m:
        ans += 1

print(ans)
