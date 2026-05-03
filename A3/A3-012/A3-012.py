n, s = map(int, input().split())
forward = [0] * (n + 1)

for i in range(1, n + 1):
    forward[i] = int(input())

visited = set()
current = s

while current != 0 and current not in visited:
    visited.add(current)
    current = forward[current]

print(len(visited))