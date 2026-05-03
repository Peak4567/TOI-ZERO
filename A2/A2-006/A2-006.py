N = int(input())
board = [input().strip() for _ in range(N)]

reachable = [[False]*N for _ in range(N)]

if board[N-1][N-1] == '.':
    reachable[N-1][N-1] = True

for i in reversed(range(N)):
    for j in reversed(range(N)):
        if board[i][j] == 'X':
            continue
        if (i + 1 < N and reachable[i+1][j]) or (j + 1 < N and reachable[i][j+1]) or (i == N-1 and j == N-1):
            reachable[i][j] = True
count = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == '.' and reachable[i][j]:
            count += 1

print(count)
