n, m = map(int, input().split())

grid = [input().split() for _ in range(n)]

next_grid = [row[:] for row in grid]

for i in range(n-1):
    for j in range(m):
        if grid[i][j] == '*':
            if grid[i+1][j] == '-':
                next_grid[i+1][j] = '*'

for row in next_grid:
    print(' '.join(row))
