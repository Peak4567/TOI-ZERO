n, m = map(int, input().split())

bomb_count = int(input())

grid = [['0'] * m for _ in range(n)]

bomb_positions = []
for _ in range(bomb_count):
    r, c = map(int, input().split())
    grid[r][c] = 'x'
    bomb_positions.append((r, c))

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < m

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'x':
            continue
        count = 0
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if in_bounds(nx, ny) and grid[nx][ny] == 'x':
                count += 1
        grid[i][j] = str(count)

for row in grid:
    print(' '.join(row))
